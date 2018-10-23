#!/bin/bash

if [[ $# -eq 2 ]]
then
for i in seq $2
do
( time dd if=/dev/zero of=hatem.txt bs=512000 count=$1 oflag=dsync 2>> dd.txt ) 2>> time.txt
sleep 1
done
cat dd.txt | grep -i octets | cut -d' ' -f7  |tr ',' '.'> resdisk.txt
cat time.txt | grep -i real | cut -d',' -f2 |tr 's' ' ' | sed -e 's/^/0./'> rescpu.txt

tr '\r\n' ',' < resdisk.txt > finaldisk.csv
tr '\r\n' ',' < rescpu.txt > finalcpu.csv


else
	echo -e "\nmissing count argument for dd\n please !! set count flag to number [1..N]\n"

fi