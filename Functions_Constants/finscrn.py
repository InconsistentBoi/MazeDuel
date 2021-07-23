import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, login , Level1 , Ingame_Objects, mfunc, counters

def fin(winner):
    
    running = True
    while running:
        constants.WIN.blit(constants.Blank_BG,(0,0))
        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        menubutton = constants.WIN.blit(constants.Fin2Menu_Button,(50,50))

        counters.draw_text(winner + "wins", constants.font, (255,255,255), constants.WIN, 640, 360)
        
        counters.PlayTime()

        if menubutton.collidepoint((bonk)):
            if click == True:
                mfunc.main_menu()
        
        click = False

        for event in pygame.event.get():
            if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
            # if event.type==KEYDOWN:
            #         if event.key==K_ESCAPE:
            #             running=False
            #         if event.key==K_BACKSPACE:
            #             mfunc.play_pressed()

            pygame.display.update()
            constants.Clock.tick(constants.FPS)