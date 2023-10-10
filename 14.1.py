from art import data,vs,high_low
import random
import os


game_is_continue = True
score = 0


# Length of data is 50.
def calculate_result(chosen_data_1, chosen_data_2, choice):
    """Calculates the result for who wins in terms of the followers count"""
    if choice == 'a' and chosen_data_1['follower_count'] > chosen_data_2['follower_count']:
        return True
        
    elif choice == 'b' and chosen_data_2['follower_count'] > chosen_data_1['follower_count']:
        return True
        
    
    else: 
        return False

def get_random_number(data):
    return random.randint(0,len(data)-1)

def format_data(data):
    return(f"{data['name']}, a {data['description']}, from {data['country']}")

while game_is_continue:
    # print(list(data[0].values()))
    # print(data[0])
    random_index_1 = get_random_number(data)
    chosen_data_1 = data[random_index_1]
    print(chosen_data_1)

    random_index_2 = get_random_number(data)
    chosen_data_2 = data[random_index_2]

    if chosen_data_1 == chosen_data_2:
        random_index_2 = get_random_number(data)
        chosen_data_2 = data[random_index_2]

    print(high_low)
    print(f"Compare A: {format_data(chosen_data_1)}")
    print(vs)
    print(f"Against B: {format_data(chosen_data_2)}")
    choice = input("Who has more followers? Type 'A' or 'B': " ).lower()

    result = calculate_result(chosen_data_1, chosen_data_2, choice)

    if result:
        score += 1
        os.system("clear")
        print(f"You're right! Current score: {score}") 
    else:
        os.system("clear")
        print(f"Sorry, that's wrong. Final score: {score}")
        game_is_continue = False

