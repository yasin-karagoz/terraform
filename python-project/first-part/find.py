#!/usr/bin/env python
import datetime
import subprocess
import sys
from os.path import abspath, dirname, join
from logging import info, warning
from dateutil.parser import parse

# Set PYTHONPATH so script will find wfm_k8s package
k8s_root_dir = dirname(dirname(abspath(__file__)))
sys.path.append(join(k8s_root_dir, 'python'))

from wfm_k8s.util import shell, shell_json, initialize_logging


class Wfm:

    all_wfms = []

    def __init__(self, name, cluster, url):
        self.name = name
        self.cluster = cluster
        self.url = url
        self.chart_version = None
        self.revision = None
        self.creation_date = None
        self.running = None
        self.owner = None

    @classmethod
    def find_wfm(cls, name, cluster):
        results = list(filter(lambda wfm: wfm.name == name and wfm.cluster == cluster, cls.all_wfms))
        if results:
            assert len(results) == 1
            return results[0]
        else:
            return None

    def __str__(self):
        return f'{self.cluster}/{self.name}'


class Cluster:

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_credentials(self):
        shell(f'gcloud container clusters get-credentials --zone {self.location} {self.name}')

    def can_access(self):
        """Some clusters just aren't accessible; skip them"""
        try:
            shell('kubectl version --short --request-timeout 10s > /dev/null')
            return True
        except subprocess.CalledProcessError as ex:
            if 'timeout' in str(ex).lower():
                return False
            raise ex

    @classmethod
    def all_wfm_clusters(cls):
        """Get all the k8s clusters that could potentially have WFMs in them"""
        clusters = []
        for cluster in shell_json('gcloud container clusters list --format json'):
            if 'resourceLabels' not in cluster or 'k8s_cluster_name' not in cluster['resourceLabels']:
                continue  # not a WFM domain team cluster
            clusters.append(Cluster(cluster['name'], cluster['location']))
        return sorted(clusters, key=lambda c: c.name)

    def __str__(self):
        return self.name


def all_wfms_in_dns():
    """Generate list of WFMs in all clusters by looking for DNS TXT records that
       were created by the external-dns service. Those records look like this:
          "heritage=external-dns,external-dns/owner=Keng-team-scheduling,external-dns/resource=ingress/fred-smith/fred-smith"
       There may be a few non-WFM workloads that also use external-dns. We can
       filter out those workloads by only looking for WFM backend URLs, which
       always contain "-back-k8s.".
    """
    # Note: This gcloud command takes forever. For debugging purposes, add "--limit 1000" to reduce the number of records fetched.
    all_dns_recs = shell_json('gcloud dns record-sets list --zone private-dev --format json')
    for rec in all_dns_recs:
        if rec['type'] != 'TXT' or 'heritage=external-dns' not in rec['rrdatas'][0]:
            continue
        if '-back-k8s.' not in rec['name']:
            continue  # not a WFM backend URL
        frontend_url = rec['name'].replace('-back-k8s.', '-k8s.')
        fields = {}  # extract the WFM data from the TXT record's "rrdatas" field
        for field in rec['rrdatas'][0].split(','):
            k, v = field.split('=', 2)
            fields[k] = v
        cluster = fields['external-dns/owner'][len('Keng-team-'):]  # "external-dns/owner=Keng-team-scheduling"
        name = fields['external-dns/resource'].split('/')[1]  # "external-dns/resource=ingress/fred-smith/fred-smith"
        if not frontend_url.startswith(name):
            # not sure what's going on here, but filter out these entries
            warning(f'URL does not match WFM name for WFM "{cluster}/{name}": {name} vs. {frontend_url}; skipping')
            continue
        Wfm.all_wfms.append(Wfm(name=name, cluster=cluster, url=frontend_url))


def all_wfms_in_cluster(cluster):
    cluster.get_credentials()
    if not cluster.can_access():
        info(f'Cant access {cluster} cluster; skipping')
        return
    info(f'processing WFMs in {cluster} cluster')
    all_helm_releases = shell_json('helm list -A --max 9999 -o json')
    all_wfm_releases = [release for release in all_helm_releases if release['chart'].startswith('wfm-')]
    for rel in all_wfm_releases:
        name = rel['name']
        wfm = Wfm.find_wfm(name, cluster.name)
        if not wfm:
            warning(f'No DNS record for WFM "{cluster}/{name}"; skipping')
            continue
        wfm.chart_version = rel['chart'][len('wfm-'):]
        wfm.revision = int(rel['revision'])

    all_stss = shell_json('kubectl get sts -A -o json')['items']
    all_frontends = [sts for sts in all_stss if sts['metadata']['name'] == 'frontend']
    for fe in all_frontends:
        name = fe['metadata']['namespace']
        wfm = Wfm.find_wfm(name, cluster.name)
        if not wfm:
            warning(f'No DNS record for WFM "{cluster}/{name}"; skipping')
            continue
        wfm.creation_date = parse(fe['metadata']['creationTimestamp'])
        wfm.running = fe['spec']['replicas'] == 1
        wfm.owner = fe['metadata']['labels']['owner']


def kubectl(cmd, **kwargs):
    shell('kubectl ' + cmd, **kwargs)


if __name__ == '__main__':
    initialize_logging()
    all_wfms_in_dns()
    for cluster in Cluster.all_wfm_clusters():
        #if cluster.name == "yasin-karagoz":
        all_wfms_in_cluster(cluster)
    print('################ Older than one one_month')
    one_month = datetime.timedelta(days=30)
    now = datetime.datetime.now(datetime.timezone.utc)
    with open("old-wfms.csv", "w") as f, open("email-list.properties", "w") as e:
        print('Name,Cluster,Age(days),Chart Version,Owner,Revisions,Running,URL', file=f)
        for wfm in sorted(Wfm.all_wfms, key=lambda w: str(w)):
            if not wfm.creation_date:
                warning(f'No statefulset for WFM "{wfm}"; skipping')
                continue
            age = now - wfm.creation_date
            if age > one_month:
                print(f'{wfm.name}, {wfm.cluster}, {age.days}, {wfm.chart_version},{wfm.owner}, {wfm.revision}, {wfm.running}, {wfm.url}', file=f)
                print(f'{wfm.owner}', file=e)
    with open('email-list.properties', 'r') as file:
        filedata = file.read()
        filedata = filedata.replace('.ukg.com', '@ukg.com')
    with open('email-list.properties', 'w') as file:
        file.write(filedata)
        #info(f'Deleting WFM {wfm.name}')
        #shell(f'helm uninstall {wfm.name} --namespace {wfm.name}')
        #kubectl(f'delete ns {wfm.name} --ignore-not-found=true')
