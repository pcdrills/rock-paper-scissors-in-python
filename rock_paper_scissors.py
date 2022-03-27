import random

print("Welcome to RocK -> Paper -> Scissors Game. \tmade by #pcdrills")
print (''' Options for the game are
                    1 -> Rock
                    2 -> Paper
                    3 -> Scissors
                -> Use the Number corresponding to your option
        ''')

# game options
options = ["rock", "paper", "scissors"]

# function to get the value from the user and do the validation
def get_user_value():
    user_value = 0
    while user_value < 1 or user_value > 3:
        user_value = int(input("Your Value?: "))
        if user_value < 1 or user_value > 3:
            print(f"Value ({user_value}) - Not in the range 1 -> 3")
        else:
            return user_value


# function to get the computer generated value
def get_computer_value():
    random_value = random.randint(1,3)
    return random_value

# function to check for the winnder
def check_winner(user_value, random_value):
    #conditions for testing who wins and who fails
    if (user_value == random_value):
        print("\tDraw")
    elif (user_value == 1):
        if (random_value == 2):
            print("\tComputer Wins")
        else:
            print("\tYou Win")
    elif (user_value == 2):
        if (random_value == 3):
            print("\tComputer Wins")
        else:
            print("\tYou Win")
    elif (user_value == 1):
        if (random_value == 2):
            print("\tYou Win")
        else:
            print("\tComputer Wins")


# a for loop to execute the functions thrice
for i in range(3):
    print(f"---Round {i + 1} ---")
    user_input = get_user_value()
    computer_input = get_computer_value()
    print(f"==> U: {options[user_input - 1]} vs C: {options[computer_input - 1]}")
    check_winner(user_input, computer_input)
    
        
        
    




#Rock wins against scissors
#scissors wins against paper
#paper wins against rock