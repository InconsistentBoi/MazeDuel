import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving , Ingame_Objects


def Lvl1_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    Player_Hitbox=pygame.Rect(250,590,20,20)
    Laser_Hitbox=pygame.Rect(Player_Hitbox.x,720,5,50)
    a=0
    while running:
        if a==1:
            Ingame_Objects.laser_pressed((Laser_Hitbox))
        click=False
        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)
        constants.WIN.blit(constants.Level_BG,(0,0))
        Maze=constants.WIN.blit(constants.Level1,(90,90))
        
        Laser_Button = constants.WIN.blit(constants.Laser_button,(1030,90))
        Player=constants.WIN.blit(constants.Player_Image,(Player_Hitbox.x,Player_Hitbox.y))
        Laser = constants.WIN.blit(constants.Laser,(Laser_Hitbox.x,Laser_Hitbox.y)) 
    
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT 
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
            if Laser_Button.collidepoint((bonk)):
                if click==True:
                    a=1
            if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        running=False
                        
                                
                    
        #Ingame_Objects.laser_pressed(Laser_Hitbox)
        keys_pressed=pygame.key.get_pressed()
        if Ingame_Objects.fin_line_collision(Player_Hitbox):
            pass
        Ingame_Objects.maze_collision(Player_Hitbox)
        Ingame_Objects.player_movement(keys_pressed,Player_Hitbox)
        pygame.display.update()
        constants.Clock.tick(constants.FPS)












