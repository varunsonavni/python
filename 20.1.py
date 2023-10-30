import turtle as t
import os

timmy = t.Turtle()

screen = t.Screen()

t.title("Snake Game...")
t.bgcolor("black")
# timmy.pencolor("white")
# timmy.shape("square")
# timmy.fillcolor("white")


players = []
screen.setup(width=600, height=600)
offset = 50

for i in range(3):
    player = t.Turtle(shape="square")
    player.speed("fastest")
    offset = offset - 20 
    player.penup()
    player.fillcolor("white")
    players.append(player)
    player.forward(offset)

        

def move_forward():
    speed = 20
    for i in range(3):
        players[i].forward(speed)

def move_backward():
    timmy.backward(20)

def move_clockwise():
    speed = 90
    for i in range(3):
        players[i].right(speed)
        players[i].forward(speed)

def move_anticlockwise():
    speed = 90
    for i in range(3):
        players[i].left(speed)
        players[i].forward(speed)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()  

screen.onkeypress(key="w", fun=move_forward)
screen.onkey(key="w", fun=move_forward) 

# screen.onkey(key="s", fun=move_backward) 
# screen.onkeypress(key="s", fun=move_backward)

screen.onkey(key="a", fun=move_anticlockwise) 
screen.onkeypress(key="a", fun=move_anticlockwise)


screen.onkey(key="d", fun=move_clockwise) 
screen.onkeypress(key="d", fun=move_clockwise)

screen.onkey(key="c", fun=clear) 
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
