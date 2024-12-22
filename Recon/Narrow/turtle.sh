#!/bin/bash

HOST=$1
while read fuzz;
	code=$(torsocks curl -Ls -o /dev/null -w "%{http_code}\n" "$HOST/$fuzz")
	if [ ! $code == 403 ];then
		echo "$fuzz"
	fi
done < raft.txt
