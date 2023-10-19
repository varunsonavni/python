import turtle as t
import os

timmy = t.Turtle()

screen = t.Screen()

t.title("Keyboard Game...")
t.bgcolor("white")

def move_forward():
    timmy.forward(20)

def move_backward():
    timmy.backward(20)

def move_clockwise():
    timmy.right(20)

def move_anticlockwise():
    timmy.left(20)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()  
screen.onkeypress(key="w", fun=move_forward)
screen.onkey(key="w", fun=move_forward) 

screen.onkey(key="s", fun=move_backward) 
screen.onkeypress(key="s", fun=move_backward)

screen.onkey(key="a", fun=move_anticlockwise) 
screen.onkeypress(key="a", fun=move_anticlockwise)


screen.onkey(key="d", fun=move_clockwise) 
screen.onkeypress(key="d", fun=move_clockwise)

screen.onkey(key="c", fun=clear) 
screen.onkeypress(key="c", fun=clear)

screen.exitonclick()
