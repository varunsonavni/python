# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            price = small_pizza + 2 + 1
            print(f"Your final bill is: ${price}.")
        else:  # extra_cheese == "N"
            price = small_pizza + 2
            print(f"Your final bill is: ${price}.")
    
    else:
        if extra_cheese == "Y":
            price = small_pizza + 1
            print(f"Your final bill is: ${price}.")
        else:  # extra_cheese == "N"
            price = small_pizza
            print(f"Your final bill is: ${price}.")

elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            price = medium_pizza + 3 + 1
            print(f"Your final bill is: ${price}.")
        else:  # extra_cheese == "N"
            price = medium_pizza + 3
            print(f"Your final bill is: ${price}.")
    
    else:
        if extra_cheese == "Y":
            price = medium_pizza + 1
            print(f"Your final bill is: ${price}.")
        else:  # extra_cheese == "N"
            price = medium_pizza
            print(f"Your final bill is: ${price}.")

elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            price = large_pizza + 3 + 1
            print(f"Your final bill is: ${price}.")
        else:  # extra_cheese == "N"
            price = large_pizza + 3
            print(f"Your final bill is: ${price}.")
    
    else:
        if extra_cheese == "Y":
            price = large_pizza + 1
            print(f"Your final bill is: ${price}.")
        else:  # extra_cheese == "N"
            price = large_pizza
            print(f"Your final bill is: ${price}.")

