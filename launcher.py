#test N1
import turtle
import os
turtle.bgcolor('gray')


while 1 == 1:
    login = turtle.textinput('login screen', 'type in your password')
    if login == '1234':
        while 1 == 1:
            t = turtle
            
            t.pendown
            launch = t.textinput('applauncher','enter any command you want to launch \n press the [x] to exit')
            os.system(launch)
