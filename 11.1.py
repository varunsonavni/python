from art import logo_blackjack
import os
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def play_game():
    print(logo_blackjack)


is_continue = True

while is_continue:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == 'y':
        play_game()
    