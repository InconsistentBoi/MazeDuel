import pygame,sys,os , pickle
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, register , Level , Ingame_Objects, counters , login
from Files import *
Players = []

def main_menu():
    while True:
            

            constants.WIN.blit(constants.Background,(0,0))
            counters.draw_text('Players Logged in:',constants.font,(173,230,240),constants.WIN,800,600)
            counters.draw_text('[Player1,Player2]',constants.font,(173,230,240),constants.WIN,800,630)
            counters.draw_text(str(Players),constants.font,(173,230,240),constants.WIN,800,680)
            mx,my=pygame.mouse.get_pos()
            bonk=(mx,my)

            button_play=constants.WIN.blit(constants.Image_play,(35,300))
            button_options=constants.WIN.blit(constants.Image_options,(35,450))
            button_exit=constants.WIN.blit(constants.Image_exit,(35,600))
            button_secret=constants.WIN.blit(constants.Image_Secret_Button,(655,90))
            button_credit=constants.WIN.blit(constants.Image_credit,(1,1))
            

            if button_play.collidepoint((bonk)):
                button_play=constants.WIN.blit(constants.Image_play_enlarged,(35,300))
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    play_pressed()
                    
            if button_options.collidepoint((bonk)):
                button_options=constants.WIN.blit(constants.Image_options_enlarged,(35,450))
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    options_pressed()

            if button_exit.collidepoint((bonk)):
                    button_exit=constants.WIN.blit(constants.Image_exit_enlarged,(35,600))

            if button_secret.collidepoint(bonk):
                    bin_file= os.path.join("Files","EasterEgg.bin")
                    f = open(bin_file,"rb")
                    secret_button_read = pickle.load(f)
                    counters.draw_text(secret_button_read,constants.Newfont,(255,255,255), constants.WIN, 1100,50)

            if button_credit.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    credits_pressed()

            click=False
        
            for event in pygame.event.get():
                if event.type==QUIT: #Lets you close the program via Red Cross Button in the top right
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

        button_htp = constants.WIN.blit(constants.Button_HTP,(35,130))
        button_login = constants.WIN.blit(constants.Image_login,(35,280))
        button_register=constants.WIN.blit(constants.Image_register,(35,430))
        button_fullscreen=constants.WIN.blit(constants.Image_fullscreen,(35,575))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))

        button_mute = constants.WIN.blit(constants.Mute_button,(1100,280))
        button_music1 = constants.WIN.blit(constants.Music1_button,(900,430))
        button_music2 = constants.WIN.blit(constants.Music2_button,(900,575))
        

        if button_htp.collidepoint((bonk)):
            constants.WIN.blit(constants.Button_HTP_enlarged,(35,130)) 

        if button_fullscreen.collidepoint((bonk)):
            constants.WIN.blit(constants.Image_fullscreen_enlarged,(35,575))   
        
        if button_register.collidepoint((bonk)):
            constants.WIN.blit(constants.Image_register_enlarged,(35,430))  

        if button_back.collidepoint((bonk)):
            constants.WIN.blit(constants.Image_back_enlarged,(10,5))
        
        if button_login.collidepoint(bonk):
            constants.WIN.blit(constants.Image_login_enlarged,(35,280))  

        if button_music1.collidepoint((bonk)):
            button_music1 = constants.WIN.blit(constants.Music1_button_enlarged,(900,430))

        if button_music2.collidepoint((bonk)):
            button_music2 = constants.WIN.blit(constants.Music2_button_enlarged,(900,575))

        if button_back.collidepoint((bonk)):
            button_back=constants.WIN.blit(constants.Image_back_enlarged, (10,5))

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.QUIT()
                sys.exit()
            
            if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True

            if button_htp.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    htp_pressed()

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
            
            if button_login.collidepoint((bonk)):
                if click==True:
                    Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                    Button_sound.play()
                    Button_sound.set_volume(0.1)
                    login_pressed()

            if button_mute.collidepoint((bonk)):
                if click==True:
                    pygame.mixer.stop()

            if button_music1.collidepoint((bonk)):
                if click == True:
                    pygame.mixer.stop()
                    Track1.play(-1)
                    Track1.set_volume(0.1)
        
            if button_music2.collidepoint((bonk)):
                if click == True:
                    pygame.mixer.stop()
                    Track2.play(-1)
                    Track2.set_volume(0.1)

        pygame.display.update()
        constants.Clock.tick(constants.FPS)

def fullscreen_pressed():
    pygame.display.toggle_fullscreen()
    pygame.display.update()
    constants.Clock.tick(constants.FPS)

Error_Hitbox = pygame.Rect(1280,720,5,50)
Success_Hitbox = pygame.Rect(1280,720,5,50)

def register_pressed():
    running=True
    while running:
        click=False
        constants.WIN.blit(constants.Blank_BG,(0,0))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))

        button_createacc = constants.WIN.blit(constants.Image_register,(600,375))
        button_delacc = constants.WIN.blit(constants.Image_delacc,(600, 100))

        counters.draw_text("Error",constants.font,(236,28,36),constants.WIN, Error_Hitbox.x,Error_Hitbox.y)
        counters.draw_text("Successful",constants.font,(0,255,0),constants.WIN, Success_Hitbox.x,Success_Hitbox.y)

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
                    Error_Hitbox.x = 1280
                    Error_Hitbox.y = 720
                    Success_Hitbox.x = 1280
                    Success_Hitbox.y = 720
                    Transition_moving.fadetoblack(constants.Width,constants.Height)
                    Transition_moving.fadetoscreen(constants.Width,constants.Height)
                    running=False
                    register.fieldclear()

            if button_delacc.collidepoint((bonk)):
                if click==True:
                    register.db_del()

            if event.type==KEYDOWN:
                pass
            for i in range(2):
                register.input(event, i)
            
            if button_createacc.collidepoint((bonk)):
                if click == True:
                    register.db_input()
                        
        
        for i in range(2):
            if constants.active[i]:
                constants.colour[i] = constants.rectcol_a
            else:
                constants.colour[i] = constants.rectcol_p
        
        for i in range(2):
            register.output(i)

        pygame.display.update()
        constants.Clock.tick(constants.FPS)

def login_pressed():
    running=True
    while running:
        click=False
        constants.WIN.blit(constants.Blank_BG,(0,0))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))

        button_signin = constants.WIN.blit(constants.Image_login,(600,375))

        counters.draw_text("Error logging in",constants.font,(236,28,36),constants.WIN, Error_Hitbox.x,Error_Hitbox.y)
        counters.draw_text("Successfully logged in",constants.font,(0,255,0),constants.WIN, Success_Hitbox.x,Success_Hitbox.y)

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
                    Error_Hitbox.x = 1280
                    Error_Hitbox.y = 720
                    Success_Hitbox.x = 1280
                    Success_Hitbox.y = 720
                    Transition_moving.fadetoblack(constants.Width,constants.Height)
                    Transition_moving.fadetoscreen(constants.Width,constants.Height)
                    running=False
                    login.fieldclear()

            if event.type==KEYDOWN:
                pass
            for i in range(4):
                login.input(event, i)
            
            if button_signin.collidepoint((bonk)):
                if click == True:
                    global Players
                    Players,status = login.db_log()
                    if status == True:
                        Error_Hitbox.x,Error_Hitbox.y = 1280,720
                        Success_Hitbox.x,Success_Hitbox.y = 600,200
                    else:
                        Error_Hitbox.x,Error_Hitbox.y = 600,200
                        Success_Hitbox.x,Success_Hitbox.y = 1280,720        
        
        for i in range(4):
            if constants.active[i]:
                constants.colour[i] = constants.rectcol_a
            else:
                constants.colour[i] = constants.rectcol_p
        
        for i in range(4):
            login.output(i)
        
        pygame.display.update()
        constants.Clock.tick(constants.FPS)

def credits_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    while running:
        mx,my=pygame.mouse.get_pos()
        bonk = (mx,my)

        credit=os.path.join("Files","Credits.txt")
        f_credit= open(credit,"r")
        f_credit_readlines= f_credit.readlines()

        constants.WIN.blit(constants.Blank_BG,(0,0))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))

        for i in range(1,len(f_credit_readlines)+1):
            credit_list= f_credit_readlines[i-1].replace("\n","")
            counters.draw_text(credit_list,constants.cred_font,(255,255,255), constants.WIN,200,100+20*i)

        
        if button_back.collidepoint((bonk)):
            button_back=constants.WIN.blit(constants.Image_back_enlarged, (10,5))    

        click = False


        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.QUIT
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
                if button_back.collidepoint((bonk)):
                    if click==True:
                        Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                        Button_sound.play()
                        Button_sound.set_volume(0.1)
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        running=False
                


        pygame.display.update()
        constants.Clock.tick(constants.FPS)

def htp_pressed():
    running=True
    Transition_moving.fadetoblack(constants.Width,constants.Height)
    Transition_moving.fadetoscreen(constants.Width,constants.Height)
    while running:
        mx,my=pygame.mouse.get_pos()
        bonk = (mx,my)

        constants.WIN.blit(constants.Image_HTP,(0,0))
        button_back=constants.WIN.blit(constants.Image_back,(10,5))

        for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.QUIT
                    sys.exit()
                if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        click=True
                if button_back.collidepoint((bonk)):
                    if click==True:
                        Button_sound= pygame.mixer.Sound(os.path.join('Sounds', 'Button_Click.mp3'))
                        Button_sound.play()
                        Button_sound.set_volume(0.1)
                        Transition_moving.fadetoblack(constants.Width,constants.Height)
                        Transition_moving.fadetoscreen(constants.Width,constants.Height)
                        running=False
                
        if button_back.collidepoint((bonk)):
            button_back=constants.WIN.blit(constants.Image_back_enlarged, (10,5))    
        
        click= False

        pygame.display.update()
        constants.Clock.tick(constants.FPS)



