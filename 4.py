# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Calculate base pizza price
if size == "S":
    base_price = 15
elif size == "M":
    base_price = 20
elif size == "L":
    base_price = 25
else:
    print("Invalid size selection. Please choose S, M, or L.")
    exit()  # Exit the program if the size is invalid.

# Add pepperoni cost
if add_pepperoni == "Y":
    if size == "S" or size == "M":
        base_price += 2
    elif size == "L":
        base_price += 3

# Add extra cheese cost
if extra_cheese == "Y":
    base_price += 1

# Print the final bill
print(f"Your final bill is: ${base_price}.")
  