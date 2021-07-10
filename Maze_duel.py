import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, mfunc

pygame.init()



def draw_text(text,font,color,surface,x,y):
    textobj= font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)


mfunc.main_menu()
