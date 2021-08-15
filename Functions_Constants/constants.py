import pygame,sys,os
from pygame.locals import *

pygame.init()

Clock=pygame.time.Clock()
FPS= 60
pygame.display.set_caption("Maze Duel")
Width, Height = 1280,720
WIN=pygame.display.set_mode((Width,Height))

font=pygame.font.SysFont(None,30)
Newfont = pygame.font.SysFont(None, 50)

BLACK= (0,0,0) 
WHITE = (255,255,255) 
RED= (255,0,0)
BLUE=(0,0,255)
VEL= 2
ANGLE = 0

Health = 20
Used_Sabotages = 0
Hits = 0

click=False

normal_size=(300,100)
enlarged_size=(380,120)

def scale(filename, size):
    unrefined = pygame.image.load(os.path.join("images",filename))
    return pygame.transform.scale(unrefined,size)

def rotate(filename, size, angle):
    return pygame.transform.rotate(scale(filename, size), angle)

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

Lvl2_button="L2button.png"
Lvl2_button_enlarged=scale(Lvl2_button,(360,180))

Lvl3_button="L3button.png"
Lvl3_button_enlarged=scale(Lvl3_button,(360,180))

Music1_button = scale("MusicButton1.png",(normal_size))
Music1_button_enlarged = scale("MusicButton1.png",(enlarged_size))
Music2_button = scale("MusicButton2.png",(normal_size))
Music2_button_enlarged = scale("MusicButton2.png",(enlarged_size))
#ingame objects
Player_Image_Up=scale("Playerchar.png",(26,26))
Player_Image_Right=rotate("Playerchar.png",(26,26), 270)
Player_Image_Down=rotate("Playerchar.png",(26,26), 180)
Player_Image_Left=rotate("Playerchar.png",(26,26), 90)
Player_Image=Player_Image_Up

Player_Image_NW = rotate("Playerchar.png",(26,26), 45)
Player_Image_NE = rotate("Playerchar.png",(26,26), -45)
Player_Image_SW = rotate("Playerchar.png",(26,26), 135)
Player_Image_SE = rotate("Playerchar.png",(26,26), -135)


Level_BG=scale("Level_BG.png",(Width,Height))


L1_Layout = scale("L1_Layout.png",(Width,Height))
L2_Layout = scale("L2_Layout.png",(Width,Height))
L3_Layout = scale("L3_Layout.png",(Width,Height))

Laser=scale("laserbeam.png",(9,69))
Laser_button=scale("Laserbutton.png",(220,120))

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

Fin2Menu_Button = scale("Button_Menu.png", (200,75))
FinBG = scale("FinBG.png", (1270,385))
#register screen
input_rect = [pygame.Rect(200,300,335,45), pygame.Rect(200,600,335,45), pygame.Rect(650,300,335,45), pygame.Rect(650,600,335,45)]
active = [False, False, False, False]
charcount = [0, 0, 0, 0]
user_text = ['', '', '', '']

rectcol_a = pygame.Color('white')
rectcol_p = pygame.Color('lightskyblue3')
base_font = [pygame.font.Font(None, 45), pygame.font.Font(None, 40), pygame.font.Font(None, 45), pygame.font.Font(None, 40)]
colour = [rectcol_p, rectcol_p, rectcol_p, rectcol_p]

