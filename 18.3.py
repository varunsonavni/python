import turtle as t

timmy = t.Turtle()

screen = t.Screen()

t.title("Dashed Line...")
t.bgcolor("white")

timmy.shape("turtle")
timmy.color("red")

def dashed_line():
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

for _ in range(13):
    dashed_line()

screen.exitonclick()