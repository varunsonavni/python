import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

choice = int(input("What do you choose? 0 ROCKY, 1 PAPERY, 2 SCISSORY\n"))

if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)


computer_total_choice = [rock, paper, scissors]
print("Computer chose:")

computer_choice = random.randint(0,2)
print(computer_choice)
print(computer_total_choice[computer_choice])

if choice == computer_choice:
    print("DRAW!")
elif choice > 2 or choice < 0:
    print("Please Enter a valid number!")
elif (choice == 0 and computer_choice == 2) or (choice == 1 and computer_choice == 0) or (choice == 2 and computer_choice == 1):
    print("You Win!")
else:
    print("You Lose!")



# if choice == 0:
#     if computer_choice == 0:
#         print("DRAW")
#     elif computer_choice == 1:
#         print("You Lose!")
#     else:
#         print("You win!")

# elif choice == 1:
#     if computer_choice == 0:
#         print("You win!")
#     elif computer_choice == 1:
#         print("DRAW")
#     else:
#         print("You Lose!")

# elif choice == 2:
#     if computer_choice == 0:
#         print("You lose!")
#     elif computer_choice == 1:
#         print("You win!")
#     else:
#         print("DRAW")






