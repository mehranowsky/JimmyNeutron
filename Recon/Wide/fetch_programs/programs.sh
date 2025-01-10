#!/bin/bash

url=https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/refs/heads/main/data/hackerone_data.json
repositoryCount=$(curl -s $url | jq -c | wc -c)
count=$(cat count.txt)
if [ "$count" -lt "$repositoryCount" ]; then
    echo 'mamad'
    repository=$(curl -s $url | jq -c)
    echo $repositoryCount > count.txt
    echo $websites | jq ".[] | {website}" > companies.txt
fi