import pygame
import sys
import os
from pygame.locals import *
from Functions_Constants import constants, Transition_moving, Level1




def player_movement(keys_pressed, Player_Hitbox):
    if keys_pressed[K_a]:
        if maze_collision(Player_Hitbox) != True:  # Leftttttt
            Player_Hitbox.x -= constants.VEL
            
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
            
    if keys_pressed[K_d]:
        if maze_collision(Player_Hitbox) != True:
            Player_Hitbox.x += constants.VEL
            
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
            
    if keys_pressed[K_s]:
        if maze_collision(Player_Hitbox) != True:  # down
            Player_Hitbox.y += constants.VEL
           
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
            
    if keys_pressed[K_w]:
        if maze_collision(Player_Hitbox) != True:  # up
            Player_Hitbox.y -= constants.VEL
            
        else:
            Player_Hitbox.x, Player_Hitbox.y = 250, 590
           


def maze_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x, Player_Hitbox.y)) == (255, 255, 255):
        constants.Health -= 1
        return True


def fin_line_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x, Player_Hitbox.y)) == (14, 209, 69):
        return True


def laser_collision(Player_Hitbox,Laser_Hitbox):
    if Player_Hitbox.colliderect(Laser_Hitbox):
        constants.Health -= 7
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def rocket_collision(Player_Hitbox,Rocket_Hitbox):
    if Player_Hitbox.colliderect(Rocket_Hitbox):
        constants.Health -= 11
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def landmine_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x, Player_Hitbox.y)) == (136, 0, 2):
        return True


def laser_pressed(Laser_Hitbox,a):
    Laser_Hitbox.y -= 14
    if Laser_Hitbox.y == 0:
        a=0

def rocket_pressed(Rocket_Hitbox,b):
    Rocket_Hitbox.y -= 9
    if Rocket_Hitbox.y == 0:
        b=0





