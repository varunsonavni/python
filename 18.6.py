import turtle as t
import random
timmy = t.Turtle()

screen = t.Screen()

t.title("Circle...")
t.bgcolor("white")


timmy.shape("arrow")
timmy.color("red")

# timmy.speed(10)

def draw_shape(offset):
    for i in range(int(360 / offset)):    
        custom_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        hex_color = "#{:02X}{:02X}{:02X}".format(*custom_color)
        timmy.pencolor(hex_color)
        current_heading = timmy.heading()
        timmy.circle(100)
        timmy.setheading(current_heading + offset)


timmy.speed("fastest")
draw_shape(5)

# print(timmy.position())

screen.exitonclick()