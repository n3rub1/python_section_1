# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:49:56 2023

Question 3
"""

import numpy as np
from skimage import measure
import matplotlib.pyplot as plt

#import the file
fullData = np.load("gb-alt.npy")
#measure all the contours according to the data recieved from the file
# contours = measure.find_contours(fullData, 0)
contours = measure.find_contours(fullData, 10)

#make two subplots, one for the image of the UK and on for the contours
fig, ax = plt.subplots()

#make the data which is 0 (sea level) as white, rest as terrain
fullData = np.ma.masked_where(fullData <= 10, fullData)
cmap = plt.cm.get_cmap("terrain").copy()
cmap.set_bad(color="white")

#plot the uk
ukMap = plt.imshow(fullData, interpolation="nearest", cmap=cmap)
#plot the contours
for contour in contours:
    ax.plot(contour[:, 1], contour[:, 0], linewidth=1.5, color="red")
    
#plot the colorbar and set the text
seaLevelBar = plt.colorbar()
seaLevelBar.ax.set_ylabel('Height above sea level [m]', rotation=90, loc="center", labelpad= 13)

#state which level
plt.xlabel("UK Map at [0] meters")

#remove the x and y numbers
ax.set_xticks([])
ax.set_yticks([])

#show the plot
plt.show()



# input("Enter by which level you would like to see the UK: \nOption 1: 0 meters \nOption 2: 1 meter \nOption 3: 2 meters \nOption 4: 10 meters\nOption 5: Exit program\n")