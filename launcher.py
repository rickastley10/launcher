#test N1
import turtle
import time
import os
turtle.bgcolor('gray')


while 1 == 1:
    login = turtle.textinput('login screen', 'type in your password')
    if login == '1234':
        while 1 == 1:
            t = turtle
            
            t.pendown
            launch = t.textinput('applauncher','enter a app that you want to launch \n type "list" to see the list of included apps')
            if launch == 'list':
                t.textinput('list','included apps: \n console \n list \n changebg \n logout \n launch ')
            if launch == 'logout':
                exit()
            if launch == 'console':
                print('console activated \n type exit to exit the console')
                while launch == 'console':
                    console_input = input('$> ')
                    if console_input == 'exit':
                        launch = 'list'
            if launch == 'changebg':
                chosen_bg = t.textinput('background changer', 'type the name of the picture to change to it')
                t.bgpic(chosen_bg)
            if launch == 'launch':
                launch_file = t.textinput('launch', 'type the name of the file that you want to launch')
                os.startfile(launch_file)
