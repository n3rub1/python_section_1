# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:56 2023

Question 3
"""

"""
This program needs the import of numpy, measure from skiamge and mathplotlib.pyplot modules
"""
import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

"""
Variables are declared.
- isMenu starts as True in order to loop in the menu on startup
"""

isMenu = True

"""
Functions are then declared for easier use for the menu
- downloadFileData() is used to download the file data using the provided file gb-alt.npy
- calculateContours() is used to calculate contours data using the fulldata from 
the file and the height above sea level
- calculateArea() is used to calculate the area based on the height above sea level
- plotMap() is used to plot the map using all the previously aquired data

"""

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

    sumbergedValue = ((submergedSum * 100)/originalSum)
    return "% unsubmerged: {:.1f}".format(sumbergedValue) # % of unsubmerged as a string with 2 sig figures

def plotMap(fullData, contours, height, area):
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
    
    xlabel = "UK Map at [" + str(height) +"] meter(s) and " + area + "%"
    plt.xlabel(xlabel)
    
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()

fullData = downloadFileData()

"""
Loop through the menu and wait for user input.  Display the map of the UK according
to the user's choice'
"""

while(isMenu):
    userInput = input("Enter by which level you would like to see the UK: \nOption 1: 0 meters \nOption 2: 1 meter \nOption 3: 2 meters \nOption 4: 10 meters\nOption 5: Exit program\n")
    
    userInput = int(userInput)
    
    if(userInput > 5 or userInput < 1):
        print("Invalid input")
    elif(userInput == 1):
        submergedLevel = 0
        contours = calculateContours(fullData, submergedLevel)
        area = calculateArea(fullData, submergedLevel)
        plotMap(fullData, contours, submergedLevel, area)
    elif(userInput == 2):
        submergedLevel = 1
        contours = calculateContours(fullData, submergedLevel)
        area = calculateArea(fullData, submergedLevel)
        plotMap(fullData, contours, submergedLevel, area)
    elif(userInput == 3):
        submergedLevel = 2
        contours = calculateContours(fullData, submergedLevel)
        area = calculateArea(fullData, submergedLevel)
        plotMap(fullData, contours, submergedLevel, area)
    elif(userInput == 4):
        submergedLevel = 10
        contours = calculateContours(fullData, submergedLevel)
        area = calculateArea(fullData, submergedLevel)
        plotMap(fullData, contours, submergedLevel, area)
    elif(userInput == 5):
        print("Thank you and goodbye")
        isMenu = False