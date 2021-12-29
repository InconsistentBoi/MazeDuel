import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, mfunc, SQLtest
#important
'''input and output functions identical to register file'''

def input(event, input_num):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if constants.input_rect[input_num].collidepoint(event.pos):
            constants.active[input_num] = True
        else:
            constants.active[input_num] = False

            
    if event.type==pygame.KEYDOWN:  
        if constants.active[input_num] == True:
            if event.key==pygame.K_BACKSPACE:
                constants.charcount[input_num]-=1
                constants.user_text[input_num] = constants.user_text[input_num][:-1]
                constants.active[input_num] = True
            else:
                if constants.charcount[input_num] < 10:
                    constants.user_text[input_num] += event.unicode 
                    constants.charcount[input_num]+=1
    
    



def output(output_num):
    if (output_num % 2):
        render_text = '*' * len(constants.user_text[output_num])

        
    else:
        render_text = constants.user_text[output_num]

        

    text_surface = constants.base_font[output_num].render(render_text,True,(255,242,0))
    constants.WIN.blit(text_surface,(constants.input_rect[output_num].x + 5, constants.input_rect[output_num].y + 5))
    pygame.draw.rect(constants.WIN,constants.colour[output_num],constants.input_rect[output_num],2) 



def db_log():
    try:
        PlayerList=[]
        itercount = 0
        for i in range(0,4,2):
            itercount += 1
            if SQLtest.sql_login(constants.user_text[i], constants.user_text[i+1]):
                PlayerList.append(constants.user_text[i])
                
            else:
                print('pass', itercount, 'wrong')
                return None,False
        print(PlayerList)
        # if PlayerList[2]==PlayerList[1]:
        #     PlayerList[2]=''
        #     counters.draw_text('Player 1 and 2 cannot have the same username',constants.font,(255,255,255),constants.WIN,10,200)
        return PlayerList,True
    except:
        pass

def fieldclear():
    for i in range(0,4,2):
        constants.user_text[i], constants.user_text[i+1] = '',''