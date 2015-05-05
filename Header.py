import os

# Create Header for POSCAR file, to edit change lattice vectors
# Intended for porphyrin unit with octyloxy side chains, may need to alter the atom types 

Lattice = open('Header', 'w+')

# Change Lattice Vectors
Vector_X = [38.0, 0.0, 0.0]
Vector_Y = [0.0, 27.3, 0.0]
Vector_Z = [0.0, 0.0, 11.0]

# Atoms in file
Atoms = "C"+" "+"N"+" "+"Zn"+" "+"O"+" "+"H"
Lattice.write(Atoms +'\n')
Lattice.write("   " + "1.00000000" + '\n')

# Lattice Vectors
Lattice.write("    " + str(Vector_X[0]) + " " + str(Vector_X[1]) + " " + str(Vector_X[2]) + '\n')
Lattice.write("    " + str(Vector_Y[0]) + " " + str(Vector_Y[1]) + " " + str(Vector_Y[2]) + '\n')
Lattice.write("    " + str(Vector_Z[0]) + " " + str(Vector_Z[1]) + " " + str(Vector_Z[2]) + '\n')

# Amount of each atom in file
Lattice.write("  " + Atoms + '\n')
os.system("cat Zeroed.xyz | awk '/C/{ sum += 1 } END {print sum}' >> Sums")
os.system("cat Zeroed.xyz | awk '/N/{ sum += 1 } END {print sum}' >> Sums")
os.system("cat Zeroed.xyz | awk '/Zn/{ sum += 1 } END {print sum}' >> Sums")
os.system("cat Zeroed.xyz | awk '/O/{ sum += 1 } END {print sum}' >> Sums")
os.system("cat Zeroed.xyz | awk '/H/{ sum += 1 } END {print sum}' >> Sums")
Sums_Open = open('Sums', 'r')
Sums_Atoms = Sums_Open.readlines()

#Print Amounts for each atom
for line in Sums_Atoms:
    Lattice.write(" " + str(line).rstrip('\n'))
Lattice.write('\n')
Lattice.write("Cartesian")

#Delete temporary file
os.system("rm Sums")
