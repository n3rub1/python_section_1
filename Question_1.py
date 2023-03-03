# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:46:39 2023

Question 1
"""

"""
This program needs the import of the math and random modules
"""

import math
import random

"""
Firstly, the variables are declared.
- N is the number of iterations needed to approximate pi to 0.0001%.  Starting at 1.
- isCalculateN starts as true in order to have the while loop start, and only stops when it is put to False
- tolerance starts at 0.  When the tolerance is <= 0.0001, the isCalculateN will turn to False
- pts_in starts at 0 (as it did originally)
"""

#variables
N = 1
isCalculateN = True
tolerance = 0
pts_in = 0

"""
Secondly, functions are declared

- approximationOfPie() takes the parameter of the current while loop approximation value 
and returns back the tolerance.  The value is forced to a positive value by using the 
abs() method. This will make sure that the tolerance percentage calculated is returned positive.

The other function, f was given.
"""

#the tolerance of pi function
def approximationOfPi(approximation):
    """Calculates the approximation of pi and returns the tolerance"""
    return abs(((approximation - math.pi)/math.pi)) * 100

#was already implemented
def f(x):
    return math.sqrt(1. - x**2)

"""
This while loop continues to run to approximate pi until the varaible isCalculateN is false. It only
turns false when the tolerance is <= 0.0001
"""
#loop until the result is less than or equal to 0.0001
while(isCalculateN):
    xi, yi = random.random(), random.random()
    if yi <= f(xi):
        pts_in += 1
    
#approximate pi and pass the value to the formula for approximation
    approximation = 4*pts_in/N
    tolerance = approximationOfPi(approximation)
    
#if the result from the approximation is <= 0.0001, stop the loop
    if(tolerance <= 0.0001):
        isCalculateN = False

#increase the value of N for each iteration, the first iteration is 1
    if(isCalculateN):    
        N = N + 1

"""
After the while loop stopped because the tolerance is <=0.0001% the value is printed to the console
"""    

print ('It took:', N, "times to approximate pi.  The approximated value is: {:.5f}".format(approximation), "and the tolarance is {:.5f}".format(tolerance) )