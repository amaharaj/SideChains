import os

File = open('1line.xyz', 'r')
File2 = open('1line.xyz', 'r')
Copy = open('3x3_Lattice.xyz','w')

# Number of units in each direction in super cell
xUnits = 3
yUnits = 3
zUnits = 3

# Shift unit in each direction for a cubic lattice
xval = 13.5
yval = 41.5
zval = 8.5

# Determine number of atoms in file
counter = 0
for lines in File:
    counter +=1
Number_of_Atoms = (counter-2)*(xUnits*yUnits*zUnits)
Copy.write(str(Number_of_Atoms) + '\n')
Copy.write('\n')

# initialize variables
a = 0
b = 0
c = 0

File2.readline()
File2.readline()

# Make copies of the unit for a cubic lattice
for line in File2.readlines():
    print line + " ! "
    coords = line.split()
    name = coords[0]
    x1, y1, z1 = float(coords[1]), float(coords[2]), float(coords[3])

    for a in range(xUnits):  
        for b in range(yUnits):
            for c in range(zUnits):
                x, y, z = x1 +a*yval, y1 + b*xval, z1 + c*zval
                Copy.write(str(name) + " " + str(x) + " " + str(y) + " " + str(z) + '\n')
                
                c += 1
            b+=1
        a +=1
