# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:40 2023

Question 2
"""

"""
random – which is used to calculate the probability, and,
matplotlib.pyplot imported as plt – which is used to plot the graph

"""

import random
import matplotlib.pyplot as plt


"""
Variables are declared.
As requested in the question, x and y begin at 0. 
The for loop calculates these variables after each iteration

The points for the created x and y values are stored in the arrays 
xValues and yValues, respectively.

maxPoints is the maximum number of points to plot which is set to start at 90000.

"""

x = 0
y = 0
xValues = []
yValues = []
maxPoints = 90000

"""
Each function requires two parameters, x and y, and outputs a numerical result based on the equation provided in the question.
functionOne returns an array of x and y values based on (0, 0.16y)
functionTwo returns an array of x and y values based on (0.85x + 0.04y, −0.04x + 0.85y + 1.6)
functionThree returns an array of x and y values based on (0.2x − 0.26y, 0.23x + 0.22y + 1.6)
functionFour returns an array of x and y values based on (−0.15x + 0.28y, 0.26x + 0.24y + 0.44)

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
All the functions listed in the section above, are put in an array.  
The probability for each function is stored in a separate array.  
For instance, functionOne will have 0.01 probability of being chosen,
 functionTwo will have the probability of 0.85, and so on.
 
Lastly, the functions are organized into another array according to 
their likelihood of being chosen using the random.choices method. k=maxPoints
 indicates that the array has 90000 elements.

Function1 0.01 of being choosen
Function2 0.85 of being choosen
Function3 0.07 of being choosen
Function4 0.07 of being choosen
"""    
functions = [functionOne, functionTwo, functionThree, functionFour]
probability = [0.01, 0.85, 0.07, 0.07]
randomFunctionGenerator = random.choices(functions, probability, k = maxPoints)

"""
 
A for loop is used to loop through each function where each function's 
returned value is stored in the returnedList variable.  
The returnedList[0] for x and the returnedList[1] for y are used to 
extract the x and y coordinates.  The append() method is then used to add 
the values to the list of xValues and yValues.

"""

for function in randomFunctionGenerator:
    returnedList = function(x, y)
    x = returnedList[0]
    y = returnedList[1]
    xValues.append(x)
    yValues.append(y)
    
"""
The plot's aspect ratio is set to "equal," the graph is drawn using data 
from the xValues and yValues arrays, and the graph's dots are set to ".",
green colour and 0.05 in thickness.
"""

plt.axes().set_aspect("equal")
plt.scatter(xValues, yValues, marker= ".", color="green", s= 0.05)
plt.show()