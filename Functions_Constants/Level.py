import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving , Ingame_Objects, counters, finscrn, login, mfunc, SQLtest


def Lvl_pressed(Level):
    running=True

   

    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)



    Player_Hitbox=pygame.Rect(250,590,20,20)
    Laser_Hitbox=pygame.Rect(Player_Hitbox.x,720,5,50)
    Rocket_Hitbox = pygame.Rect(Player_Hitbox.x,720,50,50)
    # Strike_Hitbox=pygame.Rect(0,720,200,200)
    linestate = 0
    a,b,c,d,e=(1,1,1,1,1)
    Used_Num=2
    start_ticks=pygame.time.get_ticks()
    while running:
        counters.seconds=(pygame.time.get_ticks()-start_ticks)/1000
        constants.WIN.blit(Level,(0,0))
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
            if Level == constants.L1_Layout:
                Landmine1_Hitbox = pygame.Rect(393,365,40,40)
                Active_Landmine1=constants.WIN.blit(constants.Active_Landmine,(Landmine1_Hitbox.x,Landmine1_Hitbox.y))

            if Level == constants.L2_Layout:
                Landmine1_Hitbox = pygame.Rect(230,145,60,60)
                Active_Landmine1=constants.WIN.blit(constants.scale("activelandmine.png",(60,60)),(Landmine1_Hitbox.x,Landmine1_Hitbox.y))
            
            if Level == constants.L3_Layout:
                Landmine1_Hitbox = pygame.Rect(577,480,64,64)
                Active_Landmine1=constants.WIN.blit(constants.scale("activelandmine.png",(64,64)),(Landmine1_Hitbox.x,Landmine1_Hitbox.y))
            
            Ingame_Objects.landmine1_collision(Player_Hitbox,Landmine1_Hitbox)
        else:
            pass
        
        if d==0:
            if Level == constants.L1_Layout:
                Landmine2_Hitbox = pygame.Rect(790,565,40,40)
                Active_Landmine2=constants.WIN.blit(constants.Active_Landmine,(Landmine2_Hitbox.x,Landmine2_Hitbox.y))

            if Level == constants.L2_Layout:
                Landmine2_Hitbox = pygame.Rect(396,292,80,80)
                Active_Landmine2=constants.WIN.blit(constants.scale("activelandmine.png",(80,80)),(Landmine2_Hitbox.x,Landmine2_Hitbox.y))
                
            if Level == constants.L3_Layout:
                Landmine2_Hitbox = pygame.Rect(374,400,75,75)
                Active_Landmine2=constants.WIN.blit(constants.scale("activelandmine.png",(75,75)),(Landmine2_Hitbox.x,Landmine2_Hitbox.y))    
                        
            Ingame_Objects.landmine2_collision(Player_Hitbox,Landmine2_Hitbox)   
        else:
            pass
            
        if e==0:
            if Level == constants.L1_Layout:
                Landmine3_Hitbox = pygame.Rect(710,270,40,40)
                Active_Landmine3=constants.WIN.blit(constants.Active_Landmine,(Landmine3_Hitbox.x,Landmine3_Hitbox.y))

            if Level == constants.L2_Layout:
                Landmine3_Hitbox = pygame.Rect(406,487,70,70)
                Active_Landmine3=constants.WIN.blit(constants.scale("activelandmine.png",(70,70)),(Landmine3_Hitbox.x,Landmine3_Hitbox.y))

            if Level == constants.L3_Layout:
                Landmine3_Hitbox = pygame.Rect(365,254,74,75)
                Active_Landmine3=constants.WIN.blit(constants.scale("activelandmine.png",(74,75)),(Landmine3_Hitbox.x,Landmine3_Hitbox.y))
                
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

        # Maze=constants.WIN.blit(constants.Level1,(90,90))   
        
        Laser_Button = constants.WIN.blit(constants.Laser_button,(1030,90))

        Rocket_Button = constants.WIN.blit(constants.Rocket_button,(1030,240))

        Player=constants.WIN.blit(constants.Player_Image,(Player_Hitbox.x,Player_Hitbox.y))

        Mine_Button = constants.WIN.blit(constants.Mine_button,(1030,390))

        Mine1_Button = constants.WIN.blit(constants.Mine1_button,(1040,455))

        Mine2_Button = constants.WIN.blit(constants.Mine2_button,(1115,455))

        Mine3_Button = constants.WIN.blit(constants.Mine3_button,(1190,455))

        # Strike_Button= constants.WIN.blit(constants.Strike_button, (1030,540))

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
            if Laser_Button.collidepoint((bonk)):
                if click==True:
                    if a==1:
                        Laser_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Laser_Sound.mp3'))
                        Laser_sound.play()
                        Laser_sound.set_volume(0.05)
                        constants.Used_Sabotages += 1
                    a=0
                    

            if Rocket_Button.collidepoint((bonk)):
                if click==True:
                    if b==1:
                        Rocket_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Rocket_Fire.mp3'))
                        Rocket_sound.play()
                        Rocket_sound.set_volume(0.05)
                        constants.Used_Sabotages += 1
                    b=0
                    
                    
            if Mine1_Button.collidepoint((bonk)):
                if Used_Num>=1 and click==True and c==1:
                    c=0
                    Used_Num-=1
                    constants.Used_Sabotages += 1

            if Mine2_Button.collidepoint((bonk)):
                if Used_Num>=1 and click==True and d==1:
                    d=0
                    Used_Num-=1
                    constants.Used_Sabotages += 1

            if Mine3_Button.collidepoint((bonk)):
                if Used_Num>=1 and click==True and e==1:
                    e=0
                    Used_Num-=1
                    constants.Used_Sabotages += 1

            # if Strike_Button.collidepoint((bonk)):
            #     if click==True:
            #         f=0
            #         constants.Used_Sabotages += 1 

            if event.type==KEYDOWN:
                    if event.key==K_ESCAPE:
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        constants.Health = 20
                        running=False
                        
        
        if Level == constants.L2_Layout:
            Spin = constants.rotate("Line.png",(10,85),constants.ANGLE)
            constants.WIN.blit(Spin,(765 - Spin.get_width()/2,355 - Spin.get_width()/2))
            constants.ANGLE += 3.5

        if Level == constants.L3_Layout:
            
            Line1 = constants.rotate("Line.png",(10,85),90)
            Line2 = constants.rotate("Line.png", (10,82),-45)
            Line3 = constants.rotate("Line.png", (12,50),0)


            second = int(counters.seconds)
            if second%2==0:
                constants.WIN.blit(Line1,(144, 553))
                constants.WIN.blit(Line2,(665, 355))
                constants.WIN.blit(Line3,(543, 230))

            if second%2==1:
                constants.WIN.blit(Line1,(388, 553))
                constants.WIN.blit(Line2,(600, 415))
                constants.WIN.blit(Line3,(543, 285))
                

            


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
            Remaining_Health = constants.Health
            Hits = constants.Hits
            Sabotages = constants.Used_Sabotages

            constants.Health = 20
            constants.Hits = 0
            constants.Used_Sabotages = 0
            Player_Hitbox.x, Player_Hitbox.y = 250,590
        
            winner = "Player 1 "
            win_user = 0
            print(mfunc.Players[win_user], winner, Remaining_Health, Sabotages, Hits)
            for i in range (0,2):
                exist = SQLtest.account_check(mfunc.Players[i])
                SQLtest.stats_input(exist, mfunc.Players[i], win_user)

            finscrn.fin(winner,Remaining_Health,Sabotages, Hits)
            
            
        if constants.Health <= 0: 
            Remaining_Health = 0
            Hits = constants.Hits
            Sabotages = constants.Used_Sabotages

            constants.Health = 20
            constants.Hits = 0
            constants.Used_Sabotages = 0
            Player_Hitbox.x, Player_Hitbox.y = 250,590

            winner = "Player 2 "
            win_user = 1
            print(mfunc.Players[win_user], winner,Remaining_Health,Sabotages, Hits )
            for i in range (0,2):
                SQLtest.stats_input(SQLtest.account_check(mfunc.Players[i]), mfunc.Players[i], win_user)
            finscrn.fin(winner,Remaining_Health,Sabotages, Hits)
            

        

        pygame.display.update()
        constants.Clock.tick(constants.FPS)
        
    









