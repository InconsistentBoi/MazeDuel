import pygame
import sys
import os
from pygame.locals import *
from Functions_Constants import constants, Transition_moving, Level




def player_movement(keys_pressed, Player_Hitbox):
    if keys_pressed[K_a]:
        if maze_collision(Player_Hitbox) != True:  # Leftttttt
            Player_Hitbox.x -= constants.VEL
            constants.Player_Image = constants.Player_Image_Left
        else:
           
            constants.Player_Image = constants.Player_Image_Up
            
    if keys_pressed[K_d]:
        if maze_collision(Player_Hitbox) != True:
            Player_Hitbox.x += constants.VEL
            constants.Player_Image = constants.Player_Image_Right
            
        else:
            
            constants.Player_Image = constants.Player_Image_Up
            
    if keys_pressed[K_s]:
        if maze_collision(Player_Hitbox) != True:  # down
            Player_Hitbox.y += constants.VEL
            constants.Player_Image = constants.Player_Image_Down
           
        else:
            
            constants.Player_Image = constants.Player_Image_Up
            
    if keys_pressed[K_w]:
        if maze_collision(Player_Hitbox) != True:  # up
            Player_Hitbox.y -= constants.VEL
            constants.Player_Image = constants.Player_Image_Up
            
        else:
            constants.Player_Image = constants.Player_Image_Up

    if keys_pressed[K_w] and keys_pressed[K_a]:
        if maze_collision(Player_Hitbox) != True:
            constants.Player_Image = constants.Player_Image_NW
        else:
            
            constants.Player_Image = constants.Player_Image_Up

    if keys_pressed[K_w] and keys_pressed[K_d]:
        if maze_collision(Player_Hitbox) != True:
            constants.Player_Image = constants.Player_Image_NE
            
        else:
            
            constants.Player_Image = constants.Player_Image_Up
    
    if keys_pressed[K_s] and keys_pressed[K_a]:
        if maze_collision(Player_Hitbox) != True:
            constants.Player_Image = constants.Player_Image_SW
        else:
           
            constants.Player_Image = constants.Player_Image_Up

    if keys_pressed[K_s] and keys_pressed[K_d]:
        if maze_collision(Player_Hitbox) != True:
            constants.Player_Image = constants.Player_Image_SE
        else:
            
            constants.Player_Image = constants.Player_Image_Up


def maze_collision(Player_Hitbox):
    idk = constants.WIN.get_at((Player_Hitbox.x, Player_Hitbox.y))
    if idk == (255, 255, 255):
        constants.Health -= 1
        Player_Hitbox.x, Player_Hitbox.y = 250, 590
        return True


def fin_line_collision(Player_Hitbox):
    if constants.WIN.get_at((Player_Hitbox.x, Player_Hitbox.y)) == (14, 209, 69):
        return True


def laser_collision(Player_Hitbox,Laser_Hitbox):
    if Player_Hitbox.colliderect(Laser_Hitbox):
        constants.Health -= 7
        constants.Hits += 1
        Laser_Hitbox.x, Laser_Hitbox.y = 0, 0
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def rocket_collision(Player_Hitbox,Rocket_Hitbox):
    if Player_Hitbox.colliderect(Rocket_Hitbox):
        Explosion_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Explosion_Sound.mp3'))
        Explosion_sound.play()
        Explosion_sound.set_volume(0.2)
        constants.Health -= 10
        constants.Hits += 1
        Rocket_Hitbox.x, Rocket_Hitbox.y = 1280, 0
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def landmine1_collision(Player_Hitbox,Landmine1_Hitbox):
    if Player_Hitbox.colliderect(Landmine1_Hitbox):
        Explosion_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Explosion_Sound.mp3'))
        Explosion_sound.play()
        Explosion_sound.set_volume(0.2)
        constants.Health -= 11
        constants.Hits += 1 
        Player_Hitbox.x, Player_Hitbox.y = 250, 590
        

def landmine2_collision(Player_Hitbox,Landmine2_Hitbox):
    if Player_Hitbox.colliderect(Landmine2_Hitbox):
        Explosion_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Explosion_Sound.mp3'))
        Explosion_sound.play()
        Explosion_sound.set_volume(0.2)
        constants.Health -= 15
        constants.Hits += 1 
        Player_Hitbox.x, Player_Hitbox.y = 250, 590

def landmine3_collision(Player_Hitbox,Landmine3_Hitbox):
    if Player_Hitbox.colliderect(Landmine3_Hitbox):
        Explosion_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Explosion_Sound.mp3'))
        Explosion_sound.play()
        Explosion_sound.set_volume(0.2)
        constants.Health -= 15
        constants.Hits += 1 
        Player_Hitbox.x, Player_Hitbox.y = 250, 590


def EasterEgg_collision(Player_Hitbox,easter_egg_rect,easter_egg_triggered):
    if Player_Hitbox.colliderect(easter_egg_rect )and _:
       Celebration_sound = pygame.mixer.Sound(os.path.join('Sounds', 'Celebration_Sound.mp3')) 
       Celebration_sound.play()
       Celebration_sound.set_volume(0.2)
       easter_egg_triggered=0
#   #      counters.draw_text("Congratulations! You wasted your time to find an easter egg!",constants.Newfont,(255,255,255), constants.WIN, 450, 50)

def laser_pressed(Laser_Hitbox):
    Laser_Hitbox.y -= 15
    

def rocket_pressed(Rocket_Hitbox):
    Rocket_Hitbox.y -= 9
    





    
