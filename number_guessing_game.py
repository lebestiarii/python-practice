import random

# Generate a random number
# User makes a guess
# If not a valid integer
#   Throw an exception
# If number > input
#   Too Low
# If number < input
#   Too High

number = random.randint(1, 100)

def guess_the_number():
    user_input = ""
    while user_input != number:
        try:
            user_input = int(input("Guess the number between 1 and 100: "))
            if user_input > 100 or user_input < 1:
                print("Invalid input! Input be an integer between 1 and 100.")
            elif user_input > number:
                print("Too high!")
            elif user_input < number:
                print("Too low!")
            else:
                print("You guessed the number!")
        except ValueError:
                print("Invalid input! Input must be an integer.")

if __name__ == '__main__':
    guess_the_number()