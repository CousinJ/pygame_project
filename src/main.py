
#imports
import pygame
import UI
import settings
import sys
import os
import title_screen

pygame.init()
running = True

#title screen to start off
title_screen.main()
while running:

    
    
    pygame.display.flip()
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            running = False
            












        


