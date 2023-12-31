import turtle as t
import random
timmy = t.Turtle()

screen = t.Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.title("Dashed Line...")
t.bgcolor("white")

timmy.shape("turtle")
timmy.color("red")

def draw_shape(angle, side):
    for _ in range(side):
        timmy.forward(100)
        timmy.right(angle/side)

angle = 360

for side in range(3,10):
    timmy.pencolor(random.choice(colours))
    draw_shape(angle, side)

screen.exitonclick()