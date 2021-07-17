import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving , Ingame_Objects, counters


def Lvl1_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)

    Player_Hitbox=pygame.Rect(250,590,20,20)
    Laser_Hitbox=pygame.Rect(Player_Hitbox.x,720,5,50)
    Rocket_Hitbox = pygame.Rect(Player_Hitbox.x,720,50,50)
    
    Landmine1_Hitbox = pygame.Rect(393,365,40,40)
    Landmine2_Hitbox = pygame.Rect(790,565,40,40)
    Landmine3_Hitbox = pygame.Rect(710,270,40,40)

    a=0
    b=0
    c=0
    d=0
    e=0
    Used_Num=0
    while running:
        constants.WIN.blit(constants.L1_Layout,(0,0))
        if a==0:
            Laser_Hitbox.x=Player_Hitbox.x + 10
        else:
            Ingame_Objects.laser_pressed(Laser_Hitbox,a)
        click=False

        if b==0:
            Rocket_Hitbox.x=Player_Hitbox.x 
        else:
            Ingame_Objects.rocket_pressed(Rocket_Hitbox,b)
    
        if c==1:
            Active_Landmine1=constants.WIN.blit(constants.Active_Landmine,(Landmine1_Hitbox.x,Landmine1_Hitbox.y))
            print(Used_Num)
        else:
            pass
        
        if d==1:
            Active_Landmine2=constants.WIN.blit(constants.Active_Landmine,(Landmine2_Hitbox.x,Landmine2_Hitbox.y))
            print(Used_Num)        
        else:
            pass
            
        if e==1:
            print(Used_Num)
            Active_Landmine3=constants.WIN.blit(constants.Active_Landmine,(Landmine3_Hitbox.x,Landmine3_Hitbox.y))
        else:
            pass

        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        # constants.WIN.blit(constants.L1_Layout,(0,0))
        Maze=constants.WIN.blit(constants.Level1,(90,90))   
        
        Laser_Button = constants.WIN.blit(constants.Laser_button,(1030,90))

        Rocket_Button = constants.WIN.blit(constants.Rocket_button,(1030,240))
        Player=constants.WIN.blit(constants.Player_Image,(Player_Hitbox.x,Player_Hitbox.y))

        Mine_Button = constants.WIN.blit(constants.Mine_button,(1030,390))

        Mine1_Button = constants.WIN.blit(constants.Mine1_button,(1040,455))

        Mine2_Button = constants.WIN.blit(constants.Mine2_button,(1115,455))

        Mine3_Button = constants.WIN.blit(constants.Mine3_button,(1190,455))

        Laser = constants.WIN.blit(constants.Laser,(Laser_Hitbox.x,Laser_Hitbox.y)) 
        Rocket = constants.WIN.blit(constants.Rocket,(Rocket_Hitbox.x,Rocket_Hitbox.y))
        
        
    
    

        for event in pygame.event.get():    
            if event.type==QUIT:
                pygame.QUIT 
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
                        #print(bonk)
            if Laser_Button.collidepoint((bonk)):
                if click==True:
                    a=1

            if Rocket_Button.collidepoint((bonk)):
                if click==True:
                    b=1
                    
            if Mine1_Button.collidepoint((bonk)):
                if Used_Num<=1 and click==True:
                    c=1
                    Used_Num+=1

            if Mine2_Button.collidepoint((bonk)):
                if Used_Num<=1 and click==True:
                    d=1
                    Used_Num+=1

            if Mine3_Button.collidepoint((bonk)):
                if Used_Num<=1 and click==True:
                    e=1
                    Used_Num+=1

            if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        constants.Health = 20
                        running=False
                        
                                
                    
        keys_pressed=pygame.key.get_pressed()
        if Ingame_Objects.fin_line_collision(Player_Hitbox):
            pass
        Ingame_Objects.laser_collision(Player_Hitbox,Laser_Hitbox)
        Ingame_Objects.rocket_collision(Player_Hitbox,Rocket_Hitbox)
        Ingame_Objects.maze_collision(Player_Hitbox)
        Ingame_Objects.player_movement(keys_pressed,Player_Hitbox)
        Ingame_Objects.landmine1_collision(Player_Hitbox,Landmine1_Hitbox)
        Ingame_Objects.landmine2_collision(Player_Hitbox,Landmine2_Hitbox)
        Ingame_Objects.landmine3_collision(Player_Hitbox,Landmine3_Hitbox)


        counters.health_number()



        
        pygame.display.update()
        constants.Clock.tick(constants.FPS)
        










