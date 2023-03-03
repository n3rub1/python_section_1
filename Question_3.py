# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:56 2023

Question 3
"""

"""
numpy imported as np and is used to load the data from gb-alt.npy which 
consists of mean altitudes of 10km x 10km squares of the UK

measure from skimage to draw the contours around the unsubmerged areas of the UK

matplotlib.pyplot imported as plt and is used to plot the UK

"""
import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

isMenu = True # isMenu is used to have the menu loop indefinitely, until its value is set to False.

"""
The downloadFileData function is used to download the whole contents of the 
supplied file, “gb-alt.npy”. All of the values are loaded into the variable 
fullData using the numpy module's np.load() method.

"""

def downloadFileData():
    """returns the data from the file using np.load"""
    return np.load("gb-alt.npy")

"""
The function calculateContours is used to determine the map's contours.  
The two inputs for this function are: the whole set of data from the fullData 
variable and the height above sea level.
By utilizing the measure from skimage package and its’ method 
measure.find_contours, the map's contours are returned by this method as a 
list of x and y coordinates that reflects the contour after using the entire 
data array.
"""

def calculateContours(fullData, height):
    """returns the contours data using the fulldata from the file and the height above sea level"""
    return measure.find_contours(fullData, height)

"""
The area of the UK's submerged percentage in relation to sea level rise is 
calculated using the function calculateArea. The original data is first 
calculated by adding up all the points above 0; above sea level. 
To sum up all the inner points together, a for loop inside of another 
for loop is used, and only the points bigger than 0 are added.
The same logical sum is then performed, but the complete data is 
lowered by the amount of sea level rise, so a point that was previously 
at 0 will now be -2 if there has been a sea level rise of 2.
It concludes by returning the string representing the unsubmerged percentage 
to one significant figure.
"""

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

"""
plotMap function creates a map of the UK at a given altitude above sea level. 
The entire data set, contours, height above sea level, and area are all 
parameters that have already been calculated and passed to this function.
The program first masks any parts of the map that are below the specified height. 
It then sets up a colour map and displays the map using plt.imshow.
Afterwards, it plots contour lines on top of the map using the contours variable, 
which contains a list of contour lines.
The program also adds a colour bar to the plot, the height above sea level in
meters and the total of unsubmerged area. The program then sets the x and y axis 
ticks to empty and displays the final plot using plt.show().
"""

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

fullData = downloadFileData() #fullData is set to have the full data from the provided file gb-alt.npy

"""
The user can choose which map and which calculation of the map they would want to see by selecting them from a simple menu that calls all the functions listed above in a specific order.
    Option 1 – the map and area calculation at 0 meters
    Option 2 – the map and area calculation at 1 meter
    Option 3 – the map and area calculation at 2 meters
    Option 4 – the map and area calculation at 10 meters
    Option 5 – Exit the program
    Any other numerical input – Prints out “Invalid input”
This menu will loop indefinitely until the isMenu variable is changed to False.

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