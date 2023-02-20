# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:40 2023

Question 2
"""
import random
x = 0
y = 0
randomNumber = 0
maxPoints = 90000

def functionOne(x, y):
    """Function 1 - given"""
    return (list[0,0.16*y])

def functionTwo(x, y):
    """Function 2 - given"""
    return (list[0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6])

def functionThree(x, y):
    """Function 3 - given"""
    return (list[0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6])

def functionFour(x, y):
    """Function 4 - given"""
    return (list[-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44])
    
randomNumber = random.random()

if(randomNumber <= 0.01):
    functionOne(5,5)
elif(randomNumber >= 0.85):
    functionTwo(5,5)
else:
    functionThree(5,5)
    functionFour(5,5)

print(functionOne(5, 5))
print(functionTwo(5, 5))
print(functionThree(5,5))
print(functionFour(5, 5))
