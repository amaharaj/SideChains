import os

# Create POSCAR file from xyz format
# Must use Header.py to generate lattice vector information
# Specific to porphyrin with octyloxy side chains. Must be modified for other molecules

Lattice = open('Lattice_Size','r')
Outfile = open('2S_Cell.POSCAR', 'w')

#Read in header
Header = Lattice.readlines()

for line in Header:
    Outfile.write(str(line))

# Format POSCAR file
os.system("awk '/C/{print $2, $3, $4}' Zeroed.xyz >> POSCAR_DATA")
os.system("awk '/N/{print $2, $3, $4}' Zeroed.xyz >> POSCAR_DATA")
os.system("awk '/Zn/{print $2, $3, $4}' Zeroed.xyz >> POSCAR_DATA")
os.system("awk '/O/{print $2, $3, $4}' Zeroed.xyz >> POSCAR_DATA")
os.system("awk '/H/{print $2, $3, $4}' Zeroed.xyz >> POSCAR_DATA")


POSCAR_OPEN = open('POSCAR_DATA','r')

POSCAR = POSCAR_OPEN.readlines()

# Write to output file
for coords in POSCAR:
    Outfile.write(str(coords))

Outfile.close()

