import turtle


timmy = turtle.Turtle()

turtle.title("New Game Loaded...")
turtle.bgcolor("yellow")

print(timmy)
timmy.shape("turtle")
timmy.color("red2")
timmy.forward(200)
timmy.right(100)
timmy.forward(200)

screen = turtle.Screen()

print(screen.canvheight)

# turtle.mainloop()
screen.exitonclick()

