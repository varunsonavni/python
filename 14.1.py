from art import data,vs,high_low
import random
import os


game_is_continue = True
score = 0


# Length of data is 50.
def calculate_result(chosen_data_1, chosen_data_2, choice, score):
    if choice == 'a' and chosen_data_1['follower_count'] > chosen_data_2['follower_count']:
        score += 1
        return True
        
    elif choice == 'b' and chosen_data_2['follower_count'] > chosen_data_1['follower_count']:
        score += 1
        return True
        
    
    else: 
        # print(f"Sorry, that's wrong. Final score: {score}")
        return False


while game_is_continue:
    # print(list(data[0].values()))
# print(data[0])
    random_index_1 = random.randint(0,len(data)-1)
    chosen_data_1 = data[random_index_1]
    # print(chosen_data_1)

    random_index_2 = random.randint(0,len(data)-1)
    chosen_data_2 = data[random_index_2]

    print(high_low)
    print(f"Compare A: {chosen_data_1['name']}, a {chosen_data_1['description']}, from {chosen_data_1['country']}")
    print(vs)
    print(f"Against B: {chosen_data_2['name']}, a {chosen_data_2['description']}, from {chosen_data_2['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': " ).lower()

    result = calculate_result(chosen_data_1, chosen_data_2, choice, score)

    if result:
        score += 1
        os.system("clear")
        print(f"You're right! Current score: {score}") 
    else:
        os.system("clear")
        print(f"Sorry, that's wrong. Final score: {score}")
        break



    # if choice == 'a' and chosen_data_1['follower_count'] > chosen_data_2['follower_count']:
    #     score += 1
    #     os.system("clear")
    #     print(f"You're right! Current score: {score}") 
    #     # os.system("clear")
    
    # elif choice == 'b' and chosen_data_2['follower_count'] > chosen_data_1['follower_count']:
    #     score += 1
    #     print(f"You're right! Current score: {score}") 
        
    
    # else: 
    #     print(f"Sorry, that's wrong. Final score: {score}")
    #     break


