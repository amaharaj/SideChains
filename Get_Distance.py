# print distances onto separate files
# 5 porphyrin units away
# Zn every 54 atoms
# 159 atoms every porphyrin unit
import os 
import numpy as np
import math

back = open('Test_Coords.xyz', 'r')
Data = back.readlines()
outfile = open('Test_Out', 'w')

i = 0
os.system("awk '{if ($1 == \"Zn\") print $2, $3, $4}' Test_Coords.xyz > Zn_Data")

Zinc = open('Zn_Data','r')
read_Zn = Zinc.readlines()

Units = 10

array1 = []
array2 = []
list2_sort = []
dist_x1 = []
dist_y1 = []
dist_z1 = []
dist_x2 = []
dist_y2 = []
dist_z2 = []

distance = []
a = 0

def rearrange(list_number2, a):
    for l in list_number2:
        for i in range(Units/2):

            if i < Units/2:
                l.insert(0,l[-1])
                del l[-1]
            elif i == Units/2:
                l.insert(0,l[-1])
        list2_sort.append(l) 
    Split_Coords(list1, list2_sort)

def Split_Coords(list_number1, list_number2):
    for i in range(Units/2):
        x_coord1 = [row[i][0] for row in list_number1]
        x_coord2 = [row[i][0] for row in list_number2]

        y_coord1 = [row[i][1] for row in list_number1]
        y_coord2 = [row[i][1] for row in list_number2]

        z_coord1 = [row[i][2] for row in list_number1]
        z_coord2 = [row[i][2] for row in list_number2]


        dist_x1.append(x_coord1)
        dist_x2.append(x_coord2)

        dist_y1.append(y_coord1)
        dist_y2.append(y_coord2)

        dist_z1.append(z_coord1)
        dist_z2.append(z_coord2)

    Get_Distance(dist_x1,dist_x2,dist_y1,dist_y2,dist_z1,dist_z2)

def Get_Distance(x1,x2,y1,y2,z1,z2):

    for j in range(len(dist_x1[0])):
        for i in range(Units/2):   
            x_dist = dist_x1[i][j] - dist_x2[i][j]
            x_dist = abs(x_dist)
            

            y_dist = dist_y2[i][j] - dist_y1[i][j]
            y_dist = abs(y_dist)

            z_dist = dist_z2[i][j] - dist_z1[i][j]
            z_dist = abs(z_dist)

            total_dist = math.sqrt(x_dist**2 + y_dist**2 + z_dist**2)

            distance.append(total_dist)
            
for d in read_Zn: 
    
    line = d
    d = line.split()
    coords = d[0:3]
    coords = map(float,coords)
    array1.append(coords)
    array2.append(coords)
    a+=1

list1 = [array1[x:x+Units] for x in xrange(0,len(array1),Units)]
list2 = [array2[x:x+Units] for x in xrange(0, len(array2),Units)]

rearrange(list2, a)
distance_each_pair = [distance[x:x+Units/2] for x in xrange(0,len(distance),Units/2)]

for x in distance_each_pair:
    for i in range(Units/2):
        line = str(x[i]) +  " " 
        outfile.write(line)       
    outfile.write("\n")

back.close()
outfile.close()
