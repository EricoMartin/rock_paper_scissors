import random

# Rock beats Scissors
# Paper beats Rock
# Scissors beats Paper


def rock_paper_scissors():
    list_options = ("R", "P", "S")

    print("========================================")
    print("Welcome to Play Rock, Paper, Scissors")
    print("========================================")
    print()
    print('Select an option -> "R" for "rock", "P" for "paper", "S" for "scissors".')
    print()
    user_choice = str(input("Enter your option: "))
    pc_option = random.choice(list_options)

    dict = {"R":"1", "P":"2", "S":"3"}

    if user_choice not in list_options:
        print()
        print("Wrong Input Option! Try Again!")
        print()
        return rock_paper_scissors()
    elif user_choice in list_options:
        if user_choice == "R" and pc_option == "S":
                print("You have won the Game!!!")
                print(f'Player (ROCK) : CPU (SCISSORS)')
        elif user_choice == "P" and pc_option == "R":
                print("You have won the Game!!!")
                print(f'Player (PAPER) : CPU (ROCK)')
        elif user_choice == "S" and pc_option == "P":
                print("You have won the Game!!!")
                print(f'Player (SCISSORS) : CPU (PAPER)')
        elif user_choice == pc_option:
            print("The game is a Tie!!!")
            print(f'Player ({user_choice}) : CPU ({pc_option})')
        else:
            print("You have lost the Game!!!")
            print("PC wins!!!")
            print(f'Player ({user_choice}) : CPU ({pc_option})')

rock_paper_scissors()