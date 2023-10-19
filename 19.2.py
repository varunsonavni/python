import turtle as t
import os
import random

screen = t.Screen()


t.title("Keyboard Game...")
t.bgcolor("white")

players = []
screen.setup(width=500, height=500)
offset = 130

# def move_player(player):
#     player.forward(random.randint(10,70))
#     t.ontimer(lambda: move_player(player), random.randint(100, 1000))




color = ["red", "blue", "green", "yellow", "black"]
for i in range(5):    
    player = t.Turtle(shape="turtle")
    players.append(player)
    players[i].color(color[i]) 
    players[i].penup()
    players[i].goto(-230, offset)
    # move_player(player)
    offset -= 50 

user_input = screen.textinput(title="Make Bet", prompt="Which color will win: ")

# for player in players:
#     move_player(player)    

is_race = True
while is_race:
    for player in players:
        player.forward(random.randint(0,10))
        if player.xcor() > 230:
            is_race = False
            print(player.pencolor())
            if user_input == player.pencolor():
                print(f"You've won! The {player.pencolor()} turtle is the winner!")
            else:
                print(f"You've Lost! The {player.pencolor()} turtle is the winner!")
            

print(players)
screen.exitonclick()