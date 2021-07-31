import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, login , Level , Ingame_Objects

def draw_text(text,font,color,surface,x,y):
    textobj= font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)

def health_number():
    draw_text("Health= " + str(constants.Health),constants.font,(255,255,255), constants.WIN, 0, 0)

def laser_number(a):
    draw_text("Lasers remaining: "+ str(a), constants.font,(255,255,255),constants.WIN, 1003,220)

def rocket_number(b):
    draw_text("Rockets remaining: "+ str(b), constants.font,(255,255,255),constants.WIN, 1003,369)

def landmine_number(Used_Num):
    draw_text("Landmines remaining: "+ str(Used_Num), constants.font,(255,255,255),constants.WIN, 1003,516)

seconds=0

def PlayTime():
    draw_text("Time taken= " + str(seconds) + " seconds",constants.Newfont,(255,255,255), constants.WIN, 450, 50)

def RunningTime():
    draw_text("Time= " + str(seconds) ,constants.font,(255,255,255), constants.WIN, 550, 10)


