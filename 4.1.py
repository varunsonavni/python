import random

# random.seed(2) # random.seed() function will always return same random value to our program.
outcome = random.randint(0,1)

if outcome == 1:
    print("Heads")
elif outcome == 0:
    print("Tails")


list1 = ["varun", "randy", "roman"]

print(random.choice(list1))