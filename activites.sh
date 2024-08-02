#!/bin/bash

for name_space in `cat /Users/yasin.karagoz/activites`;
   do
     kubectl get all ${name_space}
   done
