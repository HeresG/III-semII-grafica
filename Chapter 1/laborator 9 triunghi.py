# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:47:36 2025

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
# pygame to draw the outlined polygon
pygame.draw.polygon(window, (255, 0, 0), 
                    [[300, 300], [100, 400],
                     [100, 300]], 5)
 
# Draws the surface object to the screen.
pygame.display.update()