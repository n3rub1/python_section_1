# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:46:39 2023

Question 1
"""

"""
Math – used for the calculation of π
Random – used to generate a random number between 0 to 1

"""

import math
import random

"""
N is used to determine how many times the program has to loop to 
approximate pi with a tolerance of 0.0001% or less.

isCalculateN is a Boolean that starts out with the value True. 
By doing so, it is guaranteed that the while clause runs until the 
value is set to False.

tolerance starts out with the value of 0.  Throughout the program, this 
value is modified until it is less than or equal to 0.0001%.

pts_in is a given value which is used to initialize the number of points 
within the unit circle.

"""

#variables
N = 1
isCalculateN = True
tolerance = 0
pts_in = 0

"""
Secondly, functions are declared

approximationOfPie is a function that uses the formula given in the question 
to return the tolerance using the approximation of Pi as a parameter

f is a predefined function that accepts a float value and outputs the result
 using the formula provided
"""

#the tolerance of pi function
def approximationOfPi(approximation):
    """Calculates the approximation of pi and returns the tolerance"""
    return abs(((approximation - math.pi)/math.pi)) * 100

#was already implemented
def f(x):
    return math.sqrt(1. - x**2)

"""
As long as the isCalculateN variable has the value of True, the while
statement is set to loop indefinitely. The random.random() method is used
to assign a random value between 0 and 1 to two variables, xi and yi.  
The variable pts_in is raised by one if yi is less than or equal to the 
result of the f function.
Using 4*(pts_in)/N, the approximation of pi is determined and stored in the
variable - approximation.
The approximationOfPi function receives the approximation value through its
parameters and returns back the tolerance.
If the tolerance is less than or equal to 0.0001, the variable isCalulateN 
is set the false and the while loop will not iterate again.
N is raised by 1 at the end of the loop if isCalculateN is true. This is
done to ensure that the number of iterations is accurate when the variable
is set to false for isCalculateN in the previous if statement.

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
After the loop is ready, the program prints out N, the approximated value 
and the tolerance.
"""    

print ('It took:', N, "times to approximate pi.  The approximated value is: {:.5f}".format(approximation), "and the tolarance is {:.5f}".format(tolerance) )