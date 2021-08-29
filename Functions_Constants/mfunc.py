import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, register , Level , Ingame_Objects, counters

def main_menu():

    

    while True:
            

            constants.WIN.blit(constants.Background,(0,0))

            mx,my=pygame.mouse.get_pos()
            bonk=(mx,my)

            button_play=constants.WIN.blit(constants.Image_play,(35,300))
            button_options=constants.WIN.blit(constants.Image_options,(35,450))
            button_exit=constants.WIN.blit(constants.Image_exit,(35,600))


            if button_play.collidepoint((bonk)):
                constants.WIN.blit(constants.Background,(0,0))
                button_options=constants.WIN.blit(constants.Image_options,(35,450))
                button_exit=constants.WIN.blit(constants.Image_exit,(35,600))
                button_play=constants.WIN.blit(constants.Image_play_enlarged,(35,300))
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    play_pressed()
                    
            if button_options.collidepoint((bonk)):
                constants.WIN.blit(constants.Background,(0,0))
                button_options=constants.WIN.blit(constants.Image_options_enlarged,(35,450))
                button_exit=constants.WIN.blit(constants.Image_exit,(35,600))
                button_play=constants.WIN.blit(constants.Image_play,(35,300))
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    options_pressed()

            if button_exit.collidepoint((bonk)):
                    constants.WIN.blit(constants.Background,(0,0))
                    button_exit=constants.WIN.blit(constants.Image_exit_enlarged,(35,600))
                    button_play=constants.WIN.blit(constants.Image_play,(35,300))
                    button_options=constants.WIN.blit(constants.Image_options,(35,450))

            click=False

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
                if button_exit.collidepoint((bonk)):
                    if click==True:
                        click=False
                        pygame.quit()
                        sys.exit()
                        
            pygame.display.update()
            constants.Clock.tick(constants.FPS)


def play_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    while running:
        click = False

        constants.WIN.blit(constants.Blank_BG,(0,0))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))
        button_lvl1=constants.WIN.blit(constants.Lvl1_button_enlarged,(100,285))
        button_lvl2=constants.WIN.blit(constants.Lvl2_button_enlarged,(500,285))
        button_lvl3=constants.WIN.blit(constants.Lvl3_button_enlarged,(900,285))

        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        if button_back.collidepoint((bonk)):
            button_back=constants.WIN.blit(constants.Image_back_enlarged, (10,5))



        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
            if button_lvl1.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    Level.Lvl_pressed(constants.L1_Layout)
            
            if button_lvl2.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    Level.Lvl_pressed(constants.L2_Layout)

            if button_lvl3.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    Level.Lvl_pressed(constants.L3_Layout)

            if button_back.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    Transition_moving.fadetoblack(constants.Width,constants.Height)
                    Transition_moving.fadetoscreen(constants.Width,constants.Height)
                    running=False

            if event.type==KEYDOWN:
                # if event.key==K_ESCAPE:
                #     Transition_moving.fadetoblack(constants.Width,constants.Height)
                #     Transition_moving.fadetoscreen(constants.Width,constants.Height)
                #     running=False
                pass

        pygame.display.update()
        constants.Clock.tick(constants.FPS)


def options_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    t1check, t2check = 1,1
    Track1 = pygame.mixer.Sound(os.path.join('Sounds', 'MazeTunes1.mp3'))
    Track2 = pygame.mixer.Sound(os.path.join('Sounds', 'MazeTunes2.mp3'))
    while running:
        click=False
        constants.WIN.blit(constants.Blank_BG,(0,0))

        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        button_fullscreen=constants.WIN.blit(constants.Image_fullscreen,(35,400))
        button_register=constants.WIN.blit(constants.Image_register,(35,575))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))

        button_music1 = constants.WIN.blit(constants.Music1_button,(900,400))
        button_music2 = constants.WIN.blit(constants.Music2_button,(900,575))


        if button_fullscreen.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_fullscreen_enlarged,(35,400))
            constants.WIN.blit(constants.Image_register,(35,575))
            button_back=constants.WIN.blit(constants.Image_back,(10,5))
            button_music1 = constants.WIN.blit(constants.Music1_button,(900,400))
            button_music2 = constants.WIN.blit(constants.Music2_button,(900,575))
            
        
        if button_register.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_register_enlarged,(35,575))
            button_fullscreen=constants.WIN.blit(constants.Image_fullscreen,(35,400))
            button_back=constants.WIN.blit(constants.Image_back,(10,5))
            button_music1 = constants.WIN.blit(constants.Music1_button,(900,400))
            button_music2 = constants.WIN.blit(constants.Music2_button,(900,575))
            

        if button_back.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_fullscreen,(35,400))
            constants.WIN.blit(constants.Image_register,(35,575))
            constants.WIN.blit(constants.Image_back_enlarged,(10,5))
            button_music1 = constants.WIN.blit(constants.Music1_button,(900,400))
            button_music2 = constants.WIN.blit(constants.Music2_button,(900,575))
            
#needs to have button size increase
        if button_music1.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_fullscreen,(35,400))
            constants.WIN.blit(constants.Image_register,(35,575))
            constants.WIN.blit(constants.Image_back,(10,5)) 
            button_music1 = constants.WIN.blit(constants.Music1_button_enlarged,(900,400))
            button_music2 = constants.WIN.blit(constants.Music2_button,(900,575))

        if button_music2.collidepoint((bonk)):
            constants.WIN.blit(constants.Blank_BG,(0,0))
            constants.WIN.blit(constants.Image_fullscreen,(35,400))
            constants.WIN.blit(constants.Image_register,(35,575))
            constants.WIN.blit(constants.Image_back,(10,5)) 
            button_music1 = constants.WIN.blit(constants.Music1_button,(900,400))
            button_music2 = constants.WIN.blit(constants.Music2_button_enlarged,(900,575))
                  
            

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT()
                sys.exit()

            

            if event.type==KEYDOWN:
                # if event.key==K_ESCAPE:
                #     Transition_moving.fadetoblack(constants.Width,constants.Height)
                #     Transition_moving.fadetoscreen(constants.Width,constants.Height)
                #     running=False
                pass
            
            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
            if button_fullscreen.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    fullscreen_pressed()
            if button_register.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    register_pressed()
            if button_back.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    Transition_moving.fadetoblack(constants.Width,constants.Height)
                    Transition_moving.fadetoscreen(constants.Width,constants.Height)
                    running=False

            if button_music1.collidepoint((bonk)):
                if click == True and t1check==1:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    
                    pygame.mixer.stop()
                    Track1.play(-1)
                    Track1.set_volume(0.1)
                    #Track2.stop()
                    
                    t1check = 0
                    t2check = 1
            if button_music2.collidepoint((bonk)):
                if click == True and t2check==1:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)

                    pygame.mixer.stop()
                    Track2.play(-1)
                    Track2.set_volume(0.1)
                    #Track1.stop()
                    
                    t2check = 0
                    t1check = 1

        pygame.display.update()
        constants.Clock.tick(constants.FPS)

def fullscreen_pressed():
    pygame.display.toggle_fullscreen()
    pygame.display.update()
    constants.Clock.tick(constants.FPS)

Error_Hitbox = pygame.Rect(10,10,5,50)

def register_pressed():
    running=True
    while running:
        click=False
        constants.WIN.blit(constants.Blank_BG,(0,0))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))

        button_signin = constants.WIN.blit(constants.temp_button,(600,200))

        

        counters.draw_text("haha noob",constants.font,(255,255,255),constants.WIN, Error_Hitbox.x,Error_Hitbox.y)


        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)


        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT
                sys.exit()

            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True

            if button_back.collidepoint((bonk)):
                if click==True:
                    Transition_moving.fadetoblack(constants.Width,constants.Height)
                    Transition_moving.fadetoscreen(constants.Width,constants.Height)
                    running=False

            if event.type==KEYDOWN:
                # if event.key==K_ESCAPE:
                #     Transition_moving.fadetoblack(constants.Width,constants.Height)
                #     Transition_moving.fadetoscreen(constants.Width,constants.Height)
                #     running=False
                pass
            for i in range(2):
                register.input(event, i)
            
            if button_signin.collidepoint((bonk)):
                if click == True:
                    register.db_input()
                    # Error_Hitbox = pygame.Rect(10,10,5,50)
        
        for i in range(2):
            if constants.active[i]:
                constants.colour[i] = constants.rectcol_a
            else:
                constants.colour[i] = constants.rectcol_p
        
        for i in range(2):
            register.output(i)
        
        pygame.display.update()
        constants.Clock.tick(constants.FPS)

