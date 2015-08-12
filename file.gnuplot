#!/bin/bash

load '~/scripts/Colours.py'
set autoscale
set terminal wxt persist
unset label
set key off
set xtic auto
set ytic auto
set ylabel "Total Energy (eV)"
set xlabel "Time (ps)"
plot 'Run_Data' u 1:2 with lines lt rgb "#d95319"
