import mysql.connector as sql
import pygame
from Functions_Constants import counters, constants, mfunc

def sql_input(user_text, pw_text):

    try:
        if user_text=="":
            raise Exception()
        mycon = sql.connect(host='localhost',user='root',database='mazeduel',password='password')
        cursor = mycon.cursor()
        curr_sno = 1
        try:            
            cursor.execute("select max(sno) from account;")
            curr_sno=cursor.fetchall()[0][0] + 1
        except:
            pass

        sql_command = '''insert into account values (%s, %s, %s);'''

        create = (curr_sno, user_text, pw_text)

        cursor.execute(sql_command, create)
        mycon.commit()
        mycon.close()
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 10,10

    except:
        counters.draw_text("haha noob",constants.font,(255,255,255), constants.WIN, 1000,0)
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 1000,10

def sql_login(user_text, pw_text):
    try:
        if user_text=='':
            raise Exception()
        
        mycon = sql.connect(host='localhost',user='root',database='mazeduel',password='password')
        cursor = mycon.cursor()

        sql_command = '''select uname from account where uname=%s and pword=%s;'''

        sign_in = (user_text, pw_text)

        cursor.execute(sql_command, sign_in)

        data = cursor.fetchall()
        for rec in data:
            if rec == []:
                raise Exception()
            else:
                return True
        mycon.close()
        
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 10,10
        

    except:
        counters.draw_text("haha noob",constants.font,(255,255,255), constants.WIN, 1000,0)
        mfunc.Error_Hitbox.x,mfunc.Error_Hitbox.y = 1000,10

def account_check(u_name):
    
    mycon = sql.connect(host='localhost',user='root',database='mazeduel',password='password')
    cursor = mycon.cursor()

    sql_command = '''select uname from statistics where uname=%s;'''

    verify = (u_name,)

    cursor.execute(sql_command, verify)

    data = cursor.fetchall()
    if data == []:
        exist = 0
        print(exist)
    else:
        exist = 1
        print(exist)
    return exist
    mycon.close()
    
def stats_input(exist, u_name, win_user): #pay attention to parameters while calling funtion
    print(exist, u_name, win_user)

    mycon = sql.connect(host='localhost',user='root',database='mazeduel',password='password')
    cursor = mycon.cursor()
    if exist == 0:

        sql_command = '''insert into statistics(Uname,Levels_Completed, Wins, Losses) values(%s,%s,%s,%s);'''

        update = (u_name,0,0,0)
        cursor.execute(sql_command, update)
        mycon.commit()
        exist = 1
        print(u_name,'created')

    if exist == 1:
        if u_name == mfunc.Players[win_user]:
            win = 1
            loss = 0
        else:
            win = 0
            loss = 1
        sql_command = '''update statistics set Levels_completed = Levels_completed+1, Wins = Wins+%s, Losses = Losses+%s where Uname=%s;'''

        var = (win, loss, u_name)

        cursor.execute(sql_command, var)
        mycon.commit()
        print('var',var)
    mycon.close()
    
