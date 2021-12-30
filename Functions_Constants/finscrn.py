import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, register , Level , Ingame_Objects, mfunc, counters

def fin(winner, Health, Sabotages, Hits):
    
    running = True
    while running:
        constants.WIN.blit(constants.Blank_BG,(0,0))
        constants.WIN.blit(constants.FinBG,(5,330))
        mx,my=pygame.mouse.get_pos()
        bonk=(mx,my)

        menubutton = constants.WIN.blit(constants.Fin2Menu_Button,(50,50))

       #stats display 
        counters.draw_text(winner +  "wins", constants.Newfont, (255,255,255), constants.WIN, 550, 10)
        
        counters.draw_text("Successful hits: " + str(Hits),constants.Newfont, (255,255,255), constants.WIN, 950, 550)

        counters.draw_text("Sabotages avoided: " + str(Sabotages - Hits),constants.Newfont, (255,255,255), constants.WIN, 80, 550)

        counters.draw_text("Sabotages Used: " + str(Sabotages),constants.Newfont, (255,255,255), constants.WIN, 550, 475)

        counters.draw_text("Player 1 Stats:", constants.Newfont, (255,255,255), constants.WIN, 80, 350)

        counters.draw_text("Player 2 Stats:", constants.Newfont, (255,255,255), constants.WIN, 950, 350)
        
        if Health<=0:
            Health = 0
        
        counters.draw_text("Health remaining: " + str(Health), constants.Newfont, (255,255,255), constants.WIN, 80, 450)
        
        counters.draw_text("Damage done: " + str(constants.Health - Health), constants.Newfont, (255,255,255), constants.WIN, 950, 450)

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

            pygame.display.update()
            constants.Clock.tick(constants.FPS)