import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                        t  |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
entry = {}

total_bid_values = []

def calculate_score(entry):
    higest_bid = 0
    winner_person = ""

    for keys in entry:
        bid_price = entry[keys]
        if bid_price > higest_bid:
            higest_bid = bid_price
            winner = keys
   
    return(winner, winner_person, higest_bid)

    # for values in entry.values():
    #     total_bid_values.append(values)
    # return(max(total_bid_values), total_bid_values.index(max(total_bid_values)))

   

while True:
    print(logo)
    print("Welcome to Secret Aution Program")    
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    entry[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    os.system("clear")

    if other_bidders == "no":
        winner, winner_person, higest_bid = calculate_score(entry)
        print(f"The winner is {winner} with a bid of ${higest_bid}")
        break

    