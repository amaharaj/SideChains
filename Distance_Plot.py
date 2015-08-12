set encoding iso_8859_1
load 'Colours.py'
set autoscale
unset label

set linestyle 1 lt 2 lw 1
set key box linestyle 1 lc 7
set key width 0.5 height 0.75
set key top right

set xtic auto
set ytic auto
set title "Diametrically Opposed Zn Distances at 270K" font "Times-Roman,14" 
set ylabel "Distances (\305)"
set xlabel "Time (ps)"

set xrange [0:10]


plot "DISTANCES_270K" using 1:2 title '1rst pair' with lines, \
    "DISTANCES_270K" using 1:3 title '2nd pair' with lines, \
    "DISTANCES_270K" using 1:4 title '3rd pair' with lines, \
    "DISTANCES_270K" using 1:5 title '4th pair' with lines, \
    "DISTANCES_270K" using 1:6 title '5th pair' with lines
#plot 'file' u 1:2 with lines lt rgb "#d95319"
