# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:46:39 2023

Question 1
"""

import math
import random

#total number of iterations, starting from 1
N = 1
#start with the loop on true
isCalculateN = True
#start approximation, pts_in and tolerance to 0
approximation = 0
pts_in = 0
tolerance = 0

#the approximation of pi function
def approximationOfPie(approximation):
    """Calculates the approximation of pi"""
    return abs(((approximation - math.pi)/math.pi)) * 100

#was already implemented
def f(x):
    return math.sqrt(1. - x**2)

#loop until the result is less than or equal to 0.0001
while(isCalculateN):
    xi, yi = random.random(), random.random()
    if yi <= f(xi):
        pts_in += 1
    
#approximate pi and pass the value to the formula for approximation
    approximation = 4*pts_in/N
    tolerance = approximationOfPie(approximation)
    
#if the result from the approximation is <= 0.0001, stop the loop
    if(tolerance <= 0.0001):
        isCalculateN = False

#increase the value of N for each iteration, the first iteration is 1
    N = N + 1
    

print ('It took:', N, "times to approximate pi.  The approximated value is: {:.5f}".format(approximation), "and the tolarance is {:.5f}".format(tolerance) )