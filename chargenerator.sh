#!/bin/bash

# Define a string with all special characters
special_chars="!\"#$%&'()*+,-./:;<=>?@[\\]^_\`{|}~"

for (( i=0; i<${#special_chars}; i++ )); 
do 
	echo -e "${special_chars:$i:1}" 
done

echo '%0A'
echo '%00'
