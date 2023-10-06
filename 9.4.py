import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
entry = {}

total_bid_values = []

def calculate_score(entry):
    # for keys in entry:
    #     total_bid_values.append(entry[keys])


    for values in entry.values():
        total_bid_values.append(values)
    return(max(total_bid_values), total_bid_values.index(max(total_bid_values)))
    

while True:
    print(logo)
    print("Welcome to Secret Aution Program")    
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    entry[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    os.system("clear")
    if other_bidders == "no":
        winner, index = calculate_score(entry)
        # print(f"The winner is {entry[]}")
        
        break

    