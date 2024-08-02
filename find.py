#!/usr/bin/env python
import datetime
import subprocess
import sys
from os.path import abspath, dirname, join
from logging import info, warning
from dateutil.parser import parse
from argparse import ArgumentParser

# Set PYTHONPATH so script will find wfm_k8s package
k8s_root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(join(k8s_root_dir, 'python'))

from wfm_k8s.util import shell, shell_json, initialize_logging


class Wfm:

    all_wfms = []

    def __init__(self, name, cluster):
        self.name = name
        self.cluster = cluster
        self.chart_version = None
        self.revision = None
        self.creation_date = None
        self.running = None
        self.owner = None

    def __str__(self):
        return f'{self.cluster}/{self.name}'


class Cluster:
    """A GKE cluster that may contain WFM deployments"""

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.wfms = {}  # map of WFMs by WFM name

    def get_credentials(self):
        shell(f'gcloud container clusters get-credentials --zone {self.location} {self.name}')

    def can_access(self):
        """Some clusters just aren't accessible; skip them"""
        try:
            shell('kubectl version --request-timeout 10s -o json > /dev/null')
            return True
        except subprocess.CalledProcessError as ex:
            if 'timeout' in str(ex).lower():
                return False
            raise ex

    def all_wfms(self):
        """Return list of all WFMs deployed in this cluster"""
        self.all_wfms_by_helm_release()
        self.add_wfm_statefulset_data()
        return self.wfms.values()

    def all_wfms_by_helm_release(self):
        """Find all WFM Helm releases deployed in this cluster. Add each WFM to the WFMs map"""
        for rel in shell_json('helm list -a -A --max 9999 -o json'):
            if not rel['chart'].startswith('wfm-'):
                continue  # not a WFM release
            name = rel['name']
            wfm = Wfm(name, cluster.name)
            wfm.chart_version = rel['chart'][len('wfm-'):]
            wfm.revision = int(rel['revision'])
            self.wfms[name] = wfm

    def add_wfm_statefulset_data(self):
        """A WFM's Helm release doesn't contain all the info we need to process it.
           In particular, a Helm release doesn't tell us when it was initially deployed
           or who deployed it. Fetch that info from each WFM's statefulset and add it
           to the info we already obtained from the WFM's Helm release.
        """
        for sts in shell_json('kubectl get sts -A -o json')['items']:
            if sts['metadata']['name'] != 'frontend':
                continue  # not a WFM frontend
            name = sts['metadata']['namespace']
            wfm = self.wfms.get(name, None)
            if not wfm:
                info(f'WFM statefulset has no corresponding Helm release: {self}/{name}')
                continue
            wfm.creation_date = parse(sts['metadata']['creationTimestamp'])
            wfm.running = sts['spec']['replicas'] == 1
            wfm.owner = self.get_owner(sts['metadata']['labels'])

    def get_owner(self, labels):
        owner = ''
        if 'owner' in labels:
            owner = labels['owner']
            if owner.endswith('.ukg.com'):
                owner = owner.replace('.ukg.com', '@ukg.com')  # convert label value to valid email address
        return owner


    @classmethod
    def all_wfm_clusters(cls):
        """Get all the GKE clusters in the current GCP project that could potentially have WFMs in them.
           :return list of Cluster instances, sorted by name
        """
        clusters = []
        for cluster in shell_json('gcloud container clusters list --format json'):
            if 'resourceLabels' not in cluster or 'k8s_cluster_name' not in cluster['resourceLabels']:
                continue  # not a WFM domain team cluster
            clusters.append(Cluster(cluster['name'], cluster['location']))
        return sorted(clusters, key=lambda c: c.name)

    def __str__(self):
        return self.name


def kubectl(cmd, **kwargs):
    shell('kubectl ' + cmd, **kwargs)


if __name__ == '__main__':
    initialize_logging()
    parser = ArgumentParser(description='Finds and deletes old WFMs')
    parser.add_argument('--preview', help="Preview mode.", action='count', required=False)
    args = parser.parse_args()

    one_month = datetime.timedelta(days=30)
    now = datetime.datetime.now(datetime.timezone.utc)

    with open("old-wfms.csv", "w") as f, open("email-list.properties", "w") as e:
        print('Name,Cluster,Age(days),Chart Version,Owner,Revisions,Running', file=f)
        for cluster in Cluster.all_wfm_clusters():
            info(f'Looking for WFMs older than {one_month.days} days in cluster: {cluster}')
            cluster.get_credentials()
            if not cluster.can_access():
                info(f'Cant access {cluster} cluster; skipping')
                continue
            for wfm in sorted(cluster.all_wfms(), key=lambda wfm: wfm.name):
                if not wfm.creation_date:
                    warning(f'No statefulset for WFM "{wfm}"; skipping')
                    continue
                age = now - wfm.creation_date
                if age > one_month:
                    print(f'{wfm.name}, {wfm.cluster}, {age.days}, {wfm.chart_version}, {wfm.owner}, {wfm.revision}, {wfm.running}', file=f)
                    if args.preview:
                        info(f'Deleting WFM "{wfm}" because it is {age.days} days old PREVIEW ONLY')
                    else:
                        info(f'Deleting WFM "{wfm}" because it is {age.days} days old')
                        print(f'{wfm.owner}', end=", ", file=e)  # note: don't email user in preview mode
                        shell(f'helm uninstall {wfm.name} --namespace {wfm.name}')
                        kubectl(f'delete ns {wfm.name} --ignore-not-found=true')

