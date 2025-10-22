#!/bin/bash

if [ "$#" -ne 2 ]; then 
	echo "You must enter exactly 2 arguments" 
	exit 1 
fi
echo -e "\e[31m*************MY WHOIS*************\e[0m"
DOMAINS=$1
CO_NAME=$2

while read -r domain
do
	orgName=$(whois "$domain" | grep -i "OrgName" | cut -d ':' -f2)
	if echo "$orgName" | grep -i -q "$CO_NAME"; then
		echo "$domain"
	fi
done < $DOMAINS
