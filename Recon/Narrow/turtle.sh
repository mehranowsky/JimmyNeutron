#!/bin/bash

HOST=$1
block=true
num=0
while $block;
do
	code=$(curl -Ls -o /dev/null -w "%{http_code}\n" "$HOST" -L)
	if [ $code == 200 ];then
		echo "ممد نبودی ببینییی"
		printf '\a'		
		exit
	fi
	num=$(($num +1))
	echo -ne "\r$num"
	#sleep 1
done
