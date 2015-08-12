#!/usr/bin/env python
import random
inputfile = open('2S_7C_Out.xyz','r')
outputfile = open('2S_7C_Out_Rerun.xyz','w')

natoms = inputfile.readline()
outputfile.write(natoms + '\n')

scale_factor = 3

inputfile.readline()


for line in inputfile.readlines():

    coordinates = line.split()
    name = coordinates[0]
    x, y, z = float(coordinates[1]),float(coordinates[2]), float(coordinates[3])
    outputfile.write(str(name) + " " + str(x + random.random()/scale_factor) + " " + str(y + random.random()/scale_factor) + " " + str(z) + '\n')
