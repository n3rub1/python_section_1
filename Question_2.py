# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:40 2023

Question 2
"""

"""
This program needs the import of the random and mathplotlib.pyplot modules
"""

import random
import matplotlib.pyplot as plt


"""
Variables are declared.
- x starts at 0 as instructed
- y starts at 0 as instructed
- xValues is a list of all the x values and used to plot the x-axis
- yValues is a list of all the y values and used to plot the y-axis
- maxPoints was given at 90000
"""

x = 0
y = 0
xValues = []
yValues = []
maxPoints = 90000

"""
Functions are then declared for easier use during the for loop
All function return what was given.
"""

def functionOne(x, y):
    """Function 1 - given"""
    return ([0,0.16*y])

def functionTwo(x, y):
    """Function 2 - given"""
    return ([0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6])

def functionThree(x, y):
    """Function 3 - given"""
    return ([0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6])

def functionFour(x, y):
    """Function 4 - given"""
    return ([-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44])

"""
The functions are put in a list
Probabilities (given) are put in a list
Using the random.choices method, the functions are put in a list (randomFunctionGenerator)
according to their probability of being choosen.

Function1 0.01 of being choosen
Function2 0.85 of being choosen
Function3 0.07 of being choosen
Function4 0.07 of being choosen
"""    
functions = [functionOne, functionTwo, functionThree, functionFour]
probability = [0.01, 0.85, 0.07, 0.07]
randomFunctionGenerator = random.choices(functions, probability, k = maxPoints)

"""
The for loop goes through the list generated, and for each function
the function according to the index is given the x and y coordinates,
the returned value is a list, index 0 is the x and index 1 is the y.

These values are appended to the xValues and yValues array, which will
be used after to plot
"""

for function in randomFunctionGenerator:
    returnedList = function(x, y)
    x = returnedList[0]
    y = returnedList[1]
    xValues.append(x)
    yValues.append(y)
    
"""
The plot is plotted, with the aspect ratio to be equal, and the 
scatter() method is used to plot the x and y values, with a . marker,
color of green and thickness of 0.05.  Finally the plot is put
on show
"""

plt.axes().set_aspect("equal")
plt.scatter(xValues, yValues, marker= ".", color="green", s= 0.05)
plt.show()