# This is a Band Name Generator Program!

"""
Multi comment string
"""

print("Welcome to Band name Generator")
city = input("what is your city?\n")
pet = input("What is your pet name?\n")
print(f"Band name is {city} pet name is {pet}")

print("##########")
print(f"Band name is {city} pet name is \"+\" {pet}\n")  # Fstring
# print(f"Band name is {city} pet name is \"+\" {pet}\n" * 3)  # Fstring
print(("Band name is " + city + " pet name is \"+\" " + pet + "\n")) 
# print(("Band name is " + city + " pet name is \"+\" " + pet + "\n") * 3) # String concentination

# print(len(input("What is your name? ")))

division = (150/5) * 1.12

print(f"value of division of (150/5) * 1.12 is {division:.2f}") # .2f for 2 floating point value. 