import curses
from random import *

#============================= setup windows ==================================
curses.initscr()
window = curses.newwin(20,60,0,0)  #create winodow
window.keypad(1)         #use keyboard
curses.noecho()   #no echo
curses.curs_set(0)   #no use curser
window.border(0)  #boder for window
window.nodelay(1)

#============================== snake food ==================================
snake = [(9,10),(9,9),(9,8)]
food = (10,20)

score = 0
window.addch(food[0],food[1], '*')

#============================== game logic ==================================
ESC = 27
key = curses.KEY_RIGHT   #when start the game  snake go right

while key != ESC:
    window.addstr(0,10 , 'score is :'+str(score)+' ') #game Score
    window.timeout(150 - (len(snake)//5 + len(snake)//10)%120) 
    window.addstr(0,25 , 'speed = '+str(150 - (len(snake)//5 + len(snake)//10)%120)+' ') #speed snake

    prev_key = key
    event = window.getch()
    key  = event if event !=-1 else prev_key

    if key not in [curses.KEY_LEFT,curses.KEY_RIGHT ,curses.KEY_DOWN, curses.KEY_UP , ESC]:
        key = prev_key
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    elif key == curses.KEY_UP:
        y -= 1
    elif key == curses.KEY_RIGHT:
        x += 1
    elif key == curses.KEY_LEFT:
        x -= 1
    snake.insert(0,(y,x))
    if y == 0: break
    elif y == 19 : break
    elif x == 0 : break
    elif x == 59 : break
    elif snake[0] in snake[1:]:break

    if  snake[0] == food:
        score +=1
        food = ()
        while food == ():
            food = (randint(1,17), randint(1,57))
            if food in snake : food = ()
            window.addch(food[0],food[1], '*')
    else:
        last = snake.pop()
        window.addch(last[0],last[1],' ')
    window.addch(snake[0][0],snake[0][1], "#")

curses.endwin()
print(f"final score : {score}")