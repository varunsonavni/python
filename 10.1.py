import os
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def show_operations():
    operation = ["+", "-", "*", "/"]
    for symbol in operation:
        print(symbol)

is_continue  = True
final_ans_continue_bool = True

def calculate_ans(input_num_1, input_num_2, current_operation):
    """Calulate the answer of two numbers based on the current operation"""

    if current_operation == "+":
        final_ans = input_num_1 + input_num_2
        final_ans = float(f"{final_ans:.2f}")
        return final_ans
        
    elif current_operation == "-":
        final_ans = input_num_1 - input_num_2
        final_ans = float(f"{final_ans:.2f}")
        return final_ans

    elif current_operation == "*":
        final_ans = input_num_1 * input_num_2
        final_ans = float(f"{final_ans:.2f}")
        return final_ans

    elif current_operation == "/":
        final_ans = input_num_1 / input_num_2
        final_ans = float(f"{final_ans:.2f}")
        return final_ans
    
    else:
        return "Invalid operation"


def ans_format(num1, num2, operation, ans):
    print(f"{num1} {operation} {num2} = {ans}")

while is_continue:
    print(logo)
    input_num_1 = float(input("What's the first number?: "))
    show_operations()
    current_operation = input("Pick an operation: ")
    input_num_2 = float(input("What's the next number?: "))
    final_ans = calculate_ans(input_num_1, input_num_2, current_operation)
    ans_format(input_num_1, input_num_2, current_operation, final_ans)
    # print(f"{input_num_1} {current_operation} {input_num_2} = {final_ans}")
    final_ans_continue = input(f"Type 'y' to continue calculation with {final_ans}, or type 'n' to start a new calculation: ")

    if final_ans_continue == 'y':
        final_ans_continue_bool = True
        while final_ans_continue_bool:
            if final_ans_continue == 'y':
                operation = input("Pick an operation: ")
                input_num = float(input("What's the next number?: "))
                new_final_ans = calculate_ans(final_ans, input_num, operation)
                # print(f"{final_ans} {operation} {input_num} = {new_final_ans}")
                ans_format(final_ans, input_num, operation, new_final_ans)
                final_ans = new_final_ans
            else:
                final_ans_continue_bool = False
                break
            final_ans_continue = input(f"Type 'y' to continue calculation with {new_final_ans}, or type 'n' to start a new calculation: ")
    else:
        os.system("clear")




