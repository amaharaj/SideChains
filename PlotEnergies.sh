#!/bin/bash

COUNTER=1

rename 's/\d+/sprintf("%.3d",$&)/e' output.log*

for i in output.log*; do  
    grep 'Total.Energy' $i > TE`printf "%.3d" "$COUNTER"`
    let COUNTER=COUNTER+1
done

cat TE* > Total_Energy

rm TE*

awk '{print NR}' Total_Energy > file
awk '{printf "%5.10f\n", $1*0.000193504}' file > Time
awk '{printf "%5.10f\n", $3*27.211396132}' Total_Energy > Total_Energy_eV
pr -m -t -s Time Total_Energy_eV | gawk '{print $1, $2}' > Run_Data

rm file Time Total_Energy Total_Energy_eV
