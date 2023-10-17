import turtle as t

timmy = t.Turtle()

t.title("Square Creating Game...")
t.bgcolor("yellow")

timmy.shape("arrow")
timmy.color("DeepPink4")


for _ in range(4):  
    timmy.forward(200)
    timmy.right(90)



screen = t.Screen()

print(screen.canvheight)

screen.exitonclick()

