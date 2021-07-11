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
            Player_Hitbox.x,Player_Hitbox.y=250,590
    if keys_pressed[K_d]:
        if maze_collision(Player_Hitbox)!=True:
            Player_Hitbox.x += constants.VEL
        else:
            Player_Hitbox.x,Player_Hitbox.y=250,590
    if keys_pressed[K_s]:
        if maze_collision(Player_Hitbox)!=True:  # down
            Player_Hitbox.y += constants.VEL
        else:
            Player_Hitbox.x,Player_Hitbox.y=250,590
    if keys_pressed[K_w]:
        if maze_collision(Player_Hitbox)!=True:  # up
            Player_Hitbox.y -= constants.VEL
        else:
            Player_Hitbox.x,Player_Hitbox.y=250,590


def maze_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x,Player_Hitbox.y))==(255,255,255):
        return True

def fin_line_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x,Player_Hitbox.y))==(14,209,69):
        return True

def laser_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x,Player_Hitbox.y))==(100,209,233):
        return True     

def rocket_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x,Player_Hitbox.y))==(54,66,0):
        return True

def landmine_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x,Player_Hitbox.y))==(136,0,2):
        return True


def laser_pressed(Laser_Hitbox):
    Laser_Hitbox.y -= 10
    if Laser_Hitbox.y == 0:
        pass
    print("hey",Laser_Hitbox.x,Laser_Hitbox.y)
                    # constants.WIN.blit(constants.Laser,(Player_Hitbox.x,720))        