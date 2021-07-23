import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving , Ingame_Objects, counters, finscrn


def Lvl1_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)

    Player_Hitbox=pygame.Rect(250,590,20,20)
    Laser_Hitbox=pygame.Rect(Player_Hitbox.x,720,5,50)
    Rocket_Hitbox = pygame.Rect(Player_Hitbox.x,720,50,50)
    Strike_Hitbox=pygame.Rect(0,720,200,200)
    
    a,b,c,d,e=(1,1,1,1,1)
    Used_Num=2
    start_ticks=pygame.time.get_ticks()
    while running:
        counters.seconds=(pygame.time.get_ticks()-start_ticks)/1000
        constants.WIN.blit(constants.L1_Layout,(0,0))
        click=False

        if a==0:
            Ingame_Objects.laser_pressed(Laser_Hitbox)
        else:
            Laser_Hitbox.x=Player_Hitbox.x + 10

        if b==0:
            Ingame_Objects.rocket_pressed(Rocket_Hitbox)
        else:
            Rocket_Hitbox.x=Player_Hitbox.x 
    
        if c==0:
            Landmine1_Hitbox = pygame.Rect(393,365,40,40)
            Active_Landmine1=constants.WIN.blit(constants.Active_Landmine,(Landmine1_Hitbox.x,Landmine1_Hitbox.y))
            Ingame_Objects.landmine1_collision(Player_Hitbox,Landmine1_Hitbox)
        else:
            pass
        
        if d==0:
            Landmine2_Hitbox = pygame.Rect(790,565,40,40)
            Active_Landmine2=constants.WIN.blit(constants.Active_Landmine,(Landmine2_Hitbox.x,Landmine2_Hitbox.y))
            
            Ingame_Objects.landmine2_collision(Player_Hitbox,Landmine2_Hitbox)   
        else:
            pass
            
        if e==0:
            Landmine3_Hitbox = pygame.Rect(710,270,40,40)
            Active_Landmine3=constants.WIN.blit(constants.Active_Landmine,(Landmine3_Hitbox.x,Landmine3_Hitbox.y))
            Ingame_Objects.landmine3_collision(Player_Hitbox,Landmine3_Hitbox)
        else:
            pass
        
        '''if f==0:  #needs fixing
            
                Strike = constants.WIN.blit(constants.Strike,(mx-100,my-100))
                seconds=(pygame.time.get_ticks()-start_ticks)/1000 
            
                       
                Strike = constants.WIN.blit(constants.Strike,(bonk))
                
                if seconds>5:
                    Ingame_Objects.Strike_collision(Player_Hitbox)     
                print(seconds)
        else:
            Strike_Hitbox.x=Player_Hitbox.x
            Strike_Hitbox.y=Player_Hitbox.y'''
        


        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        Maze=constants.WIN.blit(constants.Level1,(90,90))   
        
        Laser_Button = constants.WIN.blit(constants.Laser_button,(1030,90))

        Rocket_Button = constants.WIN.blit(constants.Rocket_button,(1030,240))

        
        
        Player=constants.WIN.blit(constants.Player_Image,(Player_Hitbox.x,Player_Hitbox.y))

        Mine_Button = constants.WIN.blit(constants.Mine_button,(1030,390))

        Mine1_Button = constants.WIN.blit(constants.Mine1_button,(1040,455))

        Mine2_Button = constants.WIN.blit(constants.Mine2_button,(1115,455))

        Mine3_Button = constants.WIN.blit(constants.Mine3_button,(1190,455))

        Strike_Button= constants.WIN.blit(constants.Strike_button, (1030,540))

        Laser = constants.WIN.blit(constants.Laser,(Laser_Hitbox.x,Laser_Hitbox.y)) 

        Rocket = constants.WIN.blit(constants.Rocket,(Rocket_Hitbox.x,Rocket_Hitbox.y))

        # Strike = constants.WIN.blit(constants.Strike,(Strike_Hitbox.x,Strike_Hitbox.y))
        
        counters.RunningTime()
    
    

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
                    a=0 

            if Rocket_Button.collidepoint((bonk)):
                if click==True:
                    b=0
                    
            if Mine1_Button.collidepoint((bonk)):
                if Used_Num>=1 and click==True:
                    c=0
                    Used_Num-=1

            if Mine2_Button.collidepoint((bonk)):
                if Used_Num>=1 and click==True:
                    d=0
                    Used_Num-=1

            if Mine3_Button.collidepoint((bonk)):
                if Used_Num>=1 and click==True:
                    e=0
                    Used_Num-=1

            if Strike_Button.collidepoint((bonk)):
                if click==True:
                    f=0 

            if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        constants.Health = 20
                        running=False
                        
        


        keys_pressed=pygame.key.get_pressed()
        
            
        Ingame_Objects.laser_collision(Player_Hitbox,Laser_Hitbox)
        Ingame_Objects.rocket_collision(Player_Hitbox,Rocket_Hitbox)
        Ingame_Objects.maze_collision(Player_Hitbox)
        Ingame_Objects.player_movement(keys_pressed,Player_Hitbox)

        counters.health_number()
        counters.laser_number(a)
        counters.rocket_number(b)
        counters.landmine_number(Used_Num)
        
        if Ingame_Objects.fin_line_collision(Player_Hitbox):
            Remaining_Health= constants.Health
            constants.Health = 20
            Player_Hitbox.x, Player_Hitbox.y = 250,590
            winner = "Player 1 "
            finscrn.fin(winner,Remaining_Health)
            
            
        if constants.Health <= 0:
            Remaining_Health= 0
            constants.Health = 20
            Player_Hitbox.x, Player_Hitbox.y = 250,590
            winner = "Player 2 "
            finscrn.fin(winner,Remaining_Health) 

        pygame.display.update()
        constants.Clock.tick(constants.FPS)
        
    









