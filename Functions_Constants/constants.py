import pygame,sys,os
from pygame.locals import *

pygame.init()

Clock=pygame.time.Clock()
FPS= 60
pygame.display.set_caption("Maze Duel")
Width, Height = 1280,720
WIN=pygame.display.set_mode((Width,Height))

font=pygame.font.SysFont(None,30)

BLACK= (0,0,0) 
WHITE = (255,255,255) 
RED= (255,0,0)
BLUE=(0,0,255)
VEL= 2

Health = 20

click=False

normal_size=(300,100)
enlarged_size=(380,120)

def scale(filename, size):
    unrefined = pygame.image.load(os.path.join("images",filename))
    return pygame.transform.scale(unrefined,size)

#menu images
Background = scale("Background.png", (Width,Height))
Blank_BG = scale("Blank_BG.png", (Width,Height))
fname="Button_Play.png"
Image_play = scale(fname, (normal_size))
Image_play_enlarged = scale(fname, (enlarged_size))
fname="Button_Options.png"
Image_options = scale(fname, (normal_size))
Image_options_enlarged = scale(fname, (enlarged_size))
fname="Button_Exit.png"
Image_exit = scale(fname, (normal_size))
Image_exit_enlarged = scale(fname, (enlarged_size))
fname="Button_Fullscreen.png"
Image_fullscreen = scale(fname, (normal_size))
Image_fullscreen_enlarged = scale(fname, (enlarged_size))
fname="Button_Login.png"
Image_login = scale(fname, (normal_size))
Image_login_enlarged = scale(fname, (enlarged_size))
fname="Button_Back.png"
Image_back = scale(fname, (180,80))
Image_back_enlarged = scale(fname, (190,90))

fname = "Text_Bg.png"
temp_button = scale(fname, (180,80))

Lvl1_button="L1button.png"
Lvl1_button_enlarged=scale(Lvl1_button,(360,180))
Level1=scale("Level1.png",(820,540))

#ingame objects
Player_Image=scale("Playerchar.png",(20,20))

Level_BG=scale("Level_BG.png",(Width,Height))
Laser_button=scale("Laserbutton.png",(220,120))

Laser=scale("laserbeam.png",(9,69))
L1_Layout = scale("L1_Layout.png",(Width,Height))

Rocket=scale("rocket.png",(70,200))
Rocket_button=scale("Rocketbutton.png",(220,120))

Active_Landmine=scale("activelandmine.png",(45,45))

Mine_button = scale("Minebutton.png",(220,120))

Mine1_button = scale("Mine1button.png",(50,50))
Mine2_button = scale("Mine2button.png",(50,50))
Mine3_button = scale("Mine3button.png",(50,50))

Strike=scale("areastrike.png",(200,200)) #is now trap
Strike_button=scale("Strikebutton.png",(220,120))

Pause_Screen= scale("Pause.png",(Width,Height))

Fin2Menu_Button = scale("Text_Bg.png", (60,20))
#register screen
input_rect = [pygame.Rect(200,300,335,45), pygame.Rect(200,600,335,45), pygame.Rect(650,300,335,45), pygame.Rect(650,600,335,45)]
active = [False, False, False, False]
charcount = [0, 0, 0, 0]
user_text = ['', '', '', '']

rectcol_a = pygame.Color('white')
rectcol_p = pygame.Color('lightskyblue3')
base_font = [pygame.font.Font(None, 45), pygame.font.Font(None, 40), pygame.font.Font(None, 45), pygame.font.Font(None, 40)]
colour = [rectcol_p, rectcol_p, rectcol_p, rectcol_p]

