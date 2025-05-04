# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:33:01 2025

@author: gjarc
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.utilities.lambdify import lambdify, implemented_function

def aitken_neville_interpolation(currentx, x,y):
    p = np.zeros((len(y), len(y+1)))    
    p[:,0] = y
    j_len = len(y)
    for j in range(1, j_len):
        for i in range(j,j_len):
            val = (x[i]-currentx)*p[i-1,j-1]+(currentx-x[i-j])*p[i,j-1]
            p[i,j] = val/(x[i]-x[i-j])
            
    return p[-1,-1]

x = np.array([0, 2500, 5000, 10000])
y = np.array([1013, 747, 540, 226])

x1 = 1250
y1 = aitken_neville_interpolation(x1, x,y)
print('Pressure at ' + str(x1) + ' m: ' + str(y1) + ' hPa')

x2 = 3750
y2 = aitken_neville_interpolation(x2, x,y)
print('Pressure at ' + str(x2) + ' m: ' + str(y2) + ' hPa')