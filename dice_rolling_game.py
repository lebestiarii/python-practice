import random

# Ask user a question
# If user enters Y
#   Generate two random numbers
#   Print them
# If user enters n
#   Print Goodbye
#   Exit
# Else
#   Print invalid choice


def roll_dice():
    while True:
        user_input = input("Do you want to roll the dice? (Y/N): ").upper()
        if user_input == "Y":
            roll = [random.randint(1, 6), random.randint(1, 6)]
            print(f"{roll}\n")
        elif user_input == "N":
            print("Goodbye")
            break
        else:
            print("Sorry, that's not a valid input.\n")
def main():
    roll_dice()

main()