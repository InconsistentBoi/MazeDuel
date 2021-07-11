import pygame
import sys
import os
from pygame.locals import *
from Functions_Constants import constants, Transition_moving, Level1


def player_movement(keys_pressed, Player_Hitbox):
    if keys_pressed[K_a]:
        if maze_collision(Player_Hitbox)!=True:  # Leftttttt
            Player_Hitbox.x -= constants.VEL
        else:
            Player_Hitbox.x += constants.VEL + 10
    if keys_pressed[K_d]:
        if maze_collision(Player_Hitbox)!=True:
            Player_Hitbox.x += constants.VEL
        else:
            Player_Hitbox.x -= constants.VEL + 10
    if keys_pressed[K_s]:
        if maze_collision(Player_Hitbox)!=True:  # down
            Player_Hitbox.y += constants.VEL
        else:
            Player_Hitbox.y -= constants.VEL + 10
    if keys_pressed[K_w]:
        if maze_collision(Player_Hitbox)!=True:  # up
            Player_Hitbox.y -= constants.VEL
        else:
            Player_Hitbox.y += constants.VEL + 10
def maze_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x,Player_Hitbox.y))==(255,255,255):
        return True
    