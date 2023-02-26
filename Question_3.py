# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:56 2023

Question 3
"""

import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

isMenu = True

def downloadFileData():
    """returns the data from the file using np.load"""
    return np.load("gb-alt.npy")

def calculateContours(fullData, height):
    """returns the contours data using the fulldata from the file and the height above sea level"""
    return measure.find_contours(fullData, height)

def calculateArea(fullData, height):
    """calculate the area based on the height above sea level"""
    originalSum = 0
    for data in fullData:
        for subData in data:
            if(subData > 0):
                originalSum = originalSum + subData
    
    submergedSum = 0
    fullData = fullData - height
    
    for data in fullData:
        for subData in data:
            if(subData > 0):
                submergedSum = submergedSum + subData
    
    print(((submergedSum * 100)/originalSum), "% unsubmerged")
    print(100 - ((submergedSum * 100)/originalSum), "% submerged")

def plotMap(fullData, contours, height):
    """Plot the map of the UK together with the contours based on the height above sea level"""
    fig, ax = plt.subplots()
    
    fullData = np.ma.masked_where(fullData <= height, fullData)
    cmap = plt.cm.get_cmap("terrain").copy()
    cmap.set_bad(color="white")
    plt.imshow(fullData, interpolation="nearest", cmap=cmap)

    for contour in contours:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=1.5, color="red")

    seaLevelBar = plt.colorbar()
    seaLevelBar.ax.set_ylabel('Height above sea level [m]', rotation=90, loc="center", labelpad= 13)
    
    xlabel = "UK Map at [" + str(height) +"] meter(s)"
    plt.xlabel(xlabel)
    
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

fullData = downloadFileData()

while(isMenu):
    userInput = input("Enter by which level you would like to see the UK: \nOption 1: 0 meters \nOption 2: 1 meter \nOption 3: 2 meters \nOption 4: 10 meters\nOption 5: Exit program\n")
    
    userInput = int(userInput)
    
    if(userInput > 5 or userInput < 1):
        print("Invalid input")
    elif(userInput == 1):
        contours = calculateContours(fullData, 0)
        plotMap(fullData, contours, 0)
        calculateArea(fullData, 0)
    elif(userInput == 2):
        contours = calculateContours(fullData, 1)
        plotMap(fullData, contours, 1)
        calculateArea(fullData, 1)
    elif(userInput == 3):
        contours = calculateContours(fullData, 2)
        plotMap(fullData, contours, 2)
        calculateArea(fullData, 2)
    elif(userInput == 4):
        contours = calculateContours(fullData, 10)
        plotMap(fullData, contours, 10)
        calculateArea(fullData, 10)
    elif(userInput == 5):
        print("Thank you and goodbye")
        isMenu = False