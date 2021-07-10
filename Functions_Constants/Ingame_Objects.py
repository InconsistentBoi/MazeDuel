import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving , Level1

def player_movement(keys_pressed,Player):
        if keys_pressed[K_a]: #Leftttttt
            Player.x -= constants.VEL
            print(Player.x)
        if keys_pressed[K_d]:#right doing the width height bs cuz object is taken asone point intop left
            Player.x += constants.VEL
        if keys_pressed[K_s]:#down
            Player.y += constants.VEL
        if keys_pressed[K_w]:#up
            Player.y -= constants.VEL
