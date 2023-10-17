import turtle as t
import random
timmy = t.Turtle()

screen = t.Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

t.title("Random Walk...")
t.bgcolor("white")

timmy.shape("circle")
timmy.color("red")
timmy.pensize("15")

actions = [0, 90, 180, 270]

timmy.speed(10)

def draw_shape():
    timmy.forward(30)
    timmy.right(random.choice(actions))
    # timmy.setheading(random.choice(actions))

for side in range(300):
    timmy.pencolor(random.choice(colours))
    draw_shape()

screen.exitonclick()