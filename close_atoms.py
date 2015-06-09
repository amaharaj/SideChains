import os
import numpy as np
import math

Atom = open('Atoms.xyz', 'r')
Data = Atom.readlines()
Outfile = open('Results', 'w')

os.system("awk '{if ($1 == \"C\") print $2, $3, $4}' Atoms.xyz > C_Data")
os.system("awk '{if ($1 == \"O\") print $2, $3, $4}' Atoms.xyz > O_Data")
os.system("awk '{if ($1 == \"H\") print $2, $3, $4}' Atoms.xyz > H_Data")
os.system("awk '{if ($1 == \"N\") print $2, $3, $4}' Atoms.xyz > N_Data")
os.system("awk '{if ($1 == \"Zn\") print $2, $3, $4}' Atoms.xyz > Zn_Data")

Units = 10

Carbon = open('C_Data','r')
read_Carbon = Carbon.readlines()

Oxygen = open('O_Data','r')
read_Oxygen = Oxygen.readlines()

Hydrogen = open('H_Data','r')
read_Hydrogen = Hydrogen.readlines()

Nitrogen = open('N_Data','r')
read_Nitrogen = Nitrogen.readlines()

Zinc = open('Zn_Data','r')
read_Zinc = Zinc.readlines()

Steps = 3

c_array = []
c = 0
for line in read_Carbon:
    d = line
    line = d.split()
    c_coords = line[0:3]
    c_coords = map(float, c_coords)
    c_array.append(c_coords)
    c += 1
u_carbon = int(c/Steps)

o_array = []
o = 0
for line in read_Oxygen:
    d = line
    line = d.split()
    o_coords = line[0:3]
    o_coords = map(float,o_coords)
    o_array.append(o_coords)
    o += 1
u_oxygen = int(o/Steps)

h_array = []
h = 0
for line in read_Hydrogen:
    d = line
    line = d.split()
    h_coords = line[0:3]
    h_coords = map(float,h_coords)
    h_array.append(h_coords)
    h += 1
u_hydrogen = int(h/Steps)

n_array = []
n = 0
for line in read_Nitrogen:
    d = line
    line = d.split()
    n_coords = line[0:3]
    n_coords = map(float,n_coords)
    n_array.append(n_coords)
    n += 1
u_nitrogen = int(n/Steps)

z_array = []
z = 0
for line in read_Zinc:
    d = line
    line = d.split()
    z_coords = line[0:3]
    z_coords = map(float,z_coords)
    z_array.append(z_coords)
    z += 1
u_zinc = int(z/Steps)

Zn = [z_array[i:i+u_zinc] for i in range(0, len(z_array), u_zinc)] 
N = [n_array[i:i+u_nitrogen] for i in range(0, len(n_array), u_nitrogen)]
H = [h_array[i:i+u_hydrogen] for i in range(0, len(h_array), u_hydrogen)]
O = [o_array[i:i+u_oxygen] for i in range(0, len(o_array), u_oxygen)]
C = [c_array[i:i+u_carbon] for i in range(0, len(c_array), u_carbon)]

mol_coords = []
for i in range(3):
    mol_coords.append(Zn[i] + N[i] + H[i] + O[i] + C[i])

atom_dict = {}
for u in range(Units):
    atom_dict[u] = []
    u += 1

a = 0
for a in range(Steps):
    for i in range(Units):
       atom_dict[i].append(mol_coords[a][i])
    a += 1

print atom_dict

for a in range(Steps):
    for i in range(Units):
        for j in range(i+1,Units):
            print atom_dict[i][a], " - ", atom_dict[j][a]
    
