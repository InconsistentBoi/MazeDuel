import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, login , Level1 , Ingame_Objects

def draw_text(text,font,color,surface,x,y):
    textobj= font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def health_number():
    draw_text("Health= " + str(constants.Health),constants.font,(255,255,255), constants.WIN, 0, 0)








