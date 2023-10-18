import turtle as t
import random
timmy = t.Turtle()

screen = t.Screen()

t.title("Circle...")
t.bgcolor("white")

# timmy.speed(10)

def draw_circle():

    for _ in range(11): 
        timmy.pendown()
        custom_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        hex_color = "#{:02X}{:02X}{:02X}".format(*custom_color)
        # timmy.pencolor(hex_color)
        timmy.color(hex_color)   
        timmy.begin_fill()
        timmy.dot(20)
        # timmy.circle(10)
        timmy.end_fill()
        timmy.penup()
        timmy.forward(50)
        

def draw_shape(offset):
    timmy.speed("fastest")
    angle = 360
    timmy.penup()
    starting_x = -angle + 100
    starting_y = -angle + 100
    timmy.goto(starting_x, starting_y)
    starting_pos = timmy.pos()
    print(timmy.pos())  
    for i in range(9):      
        timmy.goto(starting_pos + (0, offset))
        starting_pos = timmy.pos()
        draw_circle()


print(timmy.pos())
draw_shape(50)
print(screen.window_height())
print(screen.window_width())


screen.exitonclick()