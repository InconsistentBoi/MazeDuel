import pygame
import sys
import os
from pygame.locals import *
from Functions_Constants import constants, Transition_moving, Level1


def player_movement(keys_pressed, Player_Hitbox):
    if keys_pressed[K_a]:  # Leftttttt
        Player_Hitbox.x -= constants.VEL
    if keys_pressed[K_d]:
        Player_Hitbox.x += constants.VEL
    if keys_pressed[K_s]:  # down
        Player_Hitbox.y += constants.VEL
    if keys_pressed[K_w]:  # up
        Player_Hitbox.y -= constants.VEL
