import pygame,os
from pygame.locals import *
from Functions_Constants import constants 

pygame.init()

def fadetoblack(Width,Height): 
    fade = pygame.Surface((Width, Height)) #Black surface that covers entire screen
    fade.fill((0,0,0))
    for alpha in range(0, 200,15):
        fade.set_alpha(alpha) #Sets opacity of the surface
        constants.WIN.blit(fade, (0,0))
        pygame.display.update()

def fadetoscreen(Width,Height): #Fades to screen from
    fade = pygame.Surface((Width, Height))
    fade.fill((0,0,0))
    for alpha in range(200, 0,-15):
        fade.set_alpha(alpha)
        constants.WIN.blit(fade, (0,0))
        pygame.display.update()
        constants.WIN.blit(constants.Blank_BG,(0,0))