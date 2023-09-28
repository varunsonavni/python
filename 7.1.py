import random

import os

hangman_ascii = """
 _   _    _    _   _  ____ __  __    _    _   _
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
             
"""

print(hangman_ascii)

# Words

word_list = ["aarark", "baboon", "camel", "beekeeper"]

chosen_word = random.choice(word_list)
print(chosen_word)

ans = []

for i in chosen_word:
    ans.append("_")

chance = 7

while chance > 0:
    guess = input("\nGuess a letter: ").lower()
    os.system("clear")

    for letter in range(len(chosen_word)):
        
        if chosen_word[letter] == guess:
            ans[letter] = guess
        else:
            os.system("clear")
            print("print")

        # elif chosen_word[letter] != guess:
        #     pass
        #     print("print")
        
            

    
    # os.system("clear")
    print(ans)
    if "_" not in ans:
        print("You Win!")
        break 
    chance -= 1

if "_" in ans:
    print("You Lose!")




