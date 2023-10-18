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
    # timmy.right(random.choice(actions))
    timmy.setheading(random.choice(actions))

for side in range(300):
    custom_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    print(custom_color)
    hex_color = "#{:02X}{:02X}{:02X}".format(*custom_color)
    timmy.pencolor(hex_color)
    draw_shape()

screen.exitonclick()