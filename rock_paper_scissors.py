import random

# Ask the user to make a choice
# if the choice is not valid
#     print an error
# Let the computer make a choice
# print choices
# determine the winner
# ask the user if they want to continue
# if not
#     terminate

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: '🪨', PAPER: '🧻', SCISSORS: '✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_input = str(input("\nRock, paper, or Scissors: (r/p/s) ")).lower().strip()
        if user_input not in choices:
            print("Invalid choice. Please try again.")
            continue
        else:
            return user_input

def display_choices(choice):
    computer_choice = str(random.choice(choices))
    print(f"You chose: {emojis[choice]}"
        f"\nComputer chose: {emojis[computer_choice]}")
    return computer_choice


def determine_winner(choice, computer_choice):
    if choice == computer_choice:
        print("Draw!")
    elif ((choice == ROCK and computer_choice == SCISSORS)
          or (choice == SCISSORS and computer_choice == PAPER)
          or (choice == PAPER and computer_choice == ROCK)
    ):
        print("You win!")

    elif ((choice == ROCK and computer_choice == PAPER)
          or (choice == PAPER and computer_choice == SCISSORS)
          or (choice == SCISSORS and computer_choice == ROCK)
    ):
        print("You lose!")

if __name__ == '__main__':
    while True:
        choice = get_user_choice()
        computer_choice = display_choices(choice)
        determine_winner(choice, computer_choice)
