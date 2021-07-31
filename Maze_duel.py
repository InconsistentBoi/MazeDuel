import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, mfunc

pygame.font.init()  
pygame.init()

BackgroundSound = pygame.mixer.Sound(os.path.join('Sounds', 'BG_Music.mp3'))
BackgroundSound.play(-1)
BackgroundSound.set_volume(0.05)

mfunc.main_menu()
