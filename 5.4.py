import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


let = random.choices(letters, k=nr_letters)
sym = random.choices(symbols, k=nr_symbols)
num = random.choices(numbers, k=nr_numbers)


print(let, num, sym)
password = let + sym + num
print(password)
print("")

result_string = ''.join(password)
print(f"Eassy password iss : {result_string} \n")

random.shuffle(password) # shuffle the list containing the password
print(password)
random_string2 = ''.join(password)
print(f"\n Hard password 1 iss : {random_string2} \n")



random_string = ''.join(random.sample(result_string,len(result_string)))
print(f"Hard password 2 iss : {random_string}")
