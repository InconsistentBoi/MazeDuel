import pygame,sys,os
from pygame.locals import *
from Functions_Constants import constants , Transition_moving, mfunc, SQLtest

def input(event, input_num): #Inserts text into the textbox
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
    global render_text, text_surface  #Displays the text in the textbox and censors password text
    if (output_num % 2):
        render_text = '*' * len(constants.user_text[output_num])
 
    else:
        render_text = constants.user_text[output_num]
        
    text_surface = constants.base_font[output_num].render(render_text,True,(255,242,0))
    constants.WIN.blit(text_surface,(constants.input_rect[output_num].x + 5, constants.input_rect[output_num].y + 5))
    pygame.draw.rect(constants.WIN,constants.colour[output_num],constants.input_rect[output_num],2) 


def db_log():  #Creates an account in the MySQL table 'account'
    try:
        PlayerList=[]
        itercount = 0
        for i in range(0,4,2):
            itercount += 1
            if SQLtest.sql_login(constants.user_text[i], constants.user_text[i+1]):
                PlayerList.append(constants.user_text[i])
                
            else:
                return None,False
        return PlayerList,True
    except:
        pass

def fieldclear():  #Clears the textbox text once the player exits login screen
    for i in range(4):
        constants.user_text[i] = ''
        constants.charcount[i] = 0