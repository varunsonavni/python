import turtle as t


timmy = t.Turtle()

t.title("New Game Loaded...")
t.bgcolor("yellow")

print(timmy)
timmy.shape("arrow")
timmy.color("red2")
timmy.forward(200)
timmy.right(90)
timmy.forward(200)



screen = t.Screen()

print(screen.canvheight)

print(timmy.pos())
timmy.goto(0, 0)
# t.mainloop()
screen.exitonclick()

