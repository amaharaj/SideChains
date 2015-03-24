
import os 
 
back = open('10_Constrained_Out_MD.xyz', 'r')
Data = back.readlines()
outfile = open('Distances_300K', 'w')

os.system("awk '{if ($1 == \"Zn\") print $2, $3, $4}' 10_Constrained_Out_MD.xyz > Zn_Data")

Zinc = open('Zn_Data','r')
read_Zn = Zinc.readlines()

Units = 10

array = []
a1 = []
a2 = []

a = 0 
for d in read_Zn: 
    
    line = d
    d = line.split()
    coords = d[0:3]
    coords = map(float,coords)
  
    a1.append(coords[0])
    a2.append(coords[1])

listx = [a1[x:x+Units] for x in xrange(0,len(a1),Units)]   
listy = [a2[x:x+Units] for x in xrange(0,len(a2),Units)]

for (x, y) in zip(listx, listy):

    #! /usr/bin/env python
    # -*- coding: utf-8 -*-

    """
    http://www.scipy.org/Cookbook/Least_Squares_Circle
    """

    from numpy import *

    basename = 'circle'

    # == METHOD 1 ==
    method_1 = 'algebraic'

    # coordinates of the barycenter
    x_m = mean(x)
    y_m = mean(y)

    # calculation of the reduced coordinates
    u = x - x_m
    v = y - y_m

    # linear system defining the center in reduced coordinates (uc, vc):
    #    Suu * uc +  Suv * vc = (Suuu + Suvv)/2
    #    Suv * uc +  Svv * vc = (Suuv + Svvv)/2
    Suv  = sum(u*v)
    Suu  = sum(u**2)
    Svv  = sum(v**2)
    Suuv = sum(u**2 * v)
    Suvv = sum(u * v**2)
    Suuu = sum(u**3)
    Svvv = sum(v**3)

    # Solving the linear system
    A = array([ [ Suu, Suv ], [Suv, Svv]])
    B = array([ Suuu + Suvv, Svvv + Suuv ])/2.0
    uc, vc = linalg.solve(A, B)

    xc_1 = x_m + uc
    yc_1 = y_m + vc

    # Calculation of all distances from the center (xc_1, yc_1)
    Ri_1      = sqrt((x-xc_1)**2 + (y-yc_1)**2)
    R_1       = mean(Ri_1)
    residu_1  = sum((Ri_1-R_1)**2)
    residu2_1 = sum((Ri_1**2-R_1**2)**2)

    # Decorator to count functions calls
    import functools
    def countcalls(fn):
        "decorator function count function calls "

        @functools.wraps(fn)
        def wrapped(*args):
            wrapped.ncalls +=1
            return fn(*args)

        wrapped.ncalls = 0
        return wrapped

back.close()
outfile.close()
