# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:40 2023

Question 2
"""
import random
import matplotlib.pyplot as plt

x = 0
y = 0
xValues = []
yValues = []
maxPoints = 90000

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
    
functions = [functionOne, functionTwo, functionThree, functionFour]
probability = [0.01, 0.85, 0.07, 0.07]
randomFunctionGenerator = random.choices(functions, probability, k = maxPoints)

for function in randomFunctionGenerator:
    returnedList = function(x, y)
    x = returnedList[0]
    y = returnedList[1]
    xValues.append(x)
    yValues.append(y)

plt.axes().set_aspect("equal")
plt.scatter(xValues, yValues, color="green", s= 0.05)
plt.show()