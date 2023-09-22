# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_name = name1.upper() + name2.upper()
print(combine_name)

count = 0
count2 = 0

for i in range(len(combine_name)):
    if combine_name[i] == "T" or combine_name[i] == "R" or combine_name[i] == "U" or combine_name[i] == "E":
        count += 1
    if combine_name[i] == "L" or combine_name[i] == "O" or combine_name[i] == "V" or combine_name[i] == "E":
        count2 += 1

score = int(str(count) + str(count2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
