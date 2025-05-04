# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:04:18 2025

@author: gjarc
"""

import pygame

pygame.init()
window = pygame.display.set_mode([800,600])

drag_drop = False
run = True

position = (400,300)
radius = 30
color = [50,255,60]
pygame.draw.circle(window,color,position,radius)
pygame.display.flip()

while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        if event.type ==pygame.MOUSEBUTTONDOWN:
            mouse_btn_pressed = True
            drag_drop = not drag_drop

    if (drag_drop):
        position = pygame.mouse.get_pos()
        window.fill([0,0,0])
        pygame.draw.circle(window,color,position,radius)
        pygame.display.flip()
pygame.quit()
exit()