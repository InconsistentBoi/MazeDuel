import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving


def Lvl1_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    while running:
        click=False
        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)
        constants.WIN.blit(constants.Blank_BG,(0,0))
        Maze=constants.WIN.blit(constants.Level1,(90,90))




        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT 
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
            if Maze.collidepoint((bonk)):
                if click==True:
                    print("Hello")
            if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        running=False
        pygame.display.update()
        constants.Clock.tick(constants.FPS)












