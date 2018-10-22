#!/bin/bash

if [[ $# -eq 1 ]]
then

(time dd if=/dev/zero of=hatem.txt bs=512000 count=$1 2>> dd.txt) 2>> time.txt

cat dd.txt | grep -i octets | cut -d' ' -f7  |tr ',' '.'>> resdisk.txt
cat time.txt | grep -i real | cut -d',' -f2 |tr 's' ' ' | sed -e 's/^/0./'>> rescpu.txt

tr '\r\n' ',' < resdisk.txt > finaldisk.csv
tr '\r\n' ',' < rescpu.txt > finalcpu.csv


else
	echo -e "\nmissing count argument for dd\n please !! set count flag to number [1..N]\n"

fi