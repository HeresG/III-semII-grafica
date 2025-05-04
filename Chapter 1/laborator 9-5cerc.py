# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:27:36 2025

@author: gjarc
"""

# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the solid circle
pygame.draw.circle(window, (4, 255, 255), 
				[300, 300], 60, 55)

# Draws the surface object to the screen.
pygame.display.update()
