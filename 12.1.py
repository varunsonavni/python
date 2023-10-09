from art import logo_guess_number_game
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def choose_difficulty():
    diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if diff_level == 'easy':
        return EASY_LEVEL_TURNS

    else:
        return HARD_LEVEL_TURNS


def check_answer(guess, answer, total_chances):  # 40, 20
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else: 
         print(f"You got it! The answer was {answer}.")
         return True


def play_game():
    print(logo_guess_number_game)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(answer)
    total_chances = choose_difficulty()
    print(f"You have {total_chances} attempts remaining to guess the number.")
    # print(total_chances)
    while total_chances > 0:
        total_chances -= 1
        guess = int(input("Make a guess: "))
        win = check_answer(guess, answer, total_chances)
        if win == True:
            return

        if total_chances == 0:
            print("You've run out of guesses, you lose.")
            return
        
        print("Guess again.")
        print(f"You have {total_chances} attempts remaining to guess the number.")



play_game()