import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, login , Level1 , Ingame_Objects, mfunc

def fin():
    running = True
    while running:
        constants.WIN.blit(constants.Pause_Screen,(0,0))
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        running=False
                    if event.key==K_BACKSPACE:
                        mfunc.play_pressed()
            pygame.display.update()
            constants.Clock.tick(constants.FPS)