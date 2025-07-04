# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:13:32 2025

@author: gjarc
"""

from matplotlib import pyplot as plt 
  
# DDA Function for line generation 
  
  
def DDA(x0, y0, x1, y1): 
  
    # find absolute differences 
    dx = abs(x0 - x1) 
    dy = abs(y0 - y1) 
  
    # find maximum difference 
    steps = max(dx, dy) 
  
    # calculate the increment in x and y 
    xinc = dx/steps 
    yinc = dy/steps 
  
    # start with 1st point 
    x = float(x0) 
    y = float(y0) 
  
    # make a list for coordinates 
    x_coorinates = [] 
    y_coorinates = [] 
  
    for i in range(steps): 
        # append the x,y coordinates in respective list 
        x_coorinates.append(x) 
        y_coorinates.append(y) 
  
        # increment the values 
        x = x + xinc 
        y = y + yinc 
  
    # plot the line with coordinates list 
    plt.plot(x_coorinates, y_coorinates, marker="o", 
             markersize=1, markerfacecolor="green") 
    plt.show() 
  
  
# Driver code 
if __name__ == "__main__": 
  
    # coordinates of 1st point 
    x0, y0 = 1, 2
  
    # coordinates of 2nd point 
    x1, y1 = 5, 27
  
    # Function call 
    DDA(x0, y0, x1, y1) 