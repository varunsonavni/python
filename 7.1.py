import random

import os

import wordlist

hangman_ascii = """
 _   _    _    _   _  ____ __  __    _    _   _
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
             
"""

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(hangman_ascii)

# Words

# word_list = ["aarark", "baboon", "camel", "beekeeper"]
word_list = wordlist.word_list

chosen_word = random.choice(word_list)
print(chosen_word)

ans = []

for i in chosen_word:
    ans.append("_")

chance = 6
flag = False

while chance > 0:
    guess = input("\nGuess a letter: ").lower()
    os.system("clear")

    for letter in range(len(chosen_word)):
        
        if chosen_word[letter] == guess:
            ans[letter] = guess
            flag = True

    print(ans)
    print(stages[chance])    

    if "_" not in ans:
        print("You Win!")
        break 
     
    if guess not in chosen_word:
        os.system("clear")
        print(f"You guessed {guess}, that's not in the word. You lose a life. Total Remaining life {chance}\n")
        chance -= 1
        print(stages[chance])





if "_" in ans:
    print("You Lose!")




