import math

MONTHS_IN_YEARS = 12
PERCENT = 100

def greet_user(first_name, last_name):
    print("Hello, " + first_name + " " + last_name)
    print("Welcome to the Mortgage Calculator"
          "\nPlease provide the following details"
          "\n------------------------------------")

def read_number(prompt, min, max):
    """

    :param prompt: A string that will be printed
    :param min: The minimum value expected
    :param max: The maximum value expected
    :return: The input value entered by the user
    """
    while True:
        value = int(input(prompt))
        if min <= value <= max:
            break
        print(f"Enter a value between {min} and {max}")
    return value

def calculate_mortgage(principal, annual_interest, years):
    """
    Calculate Mortgage value
    :param principal: A number between 1000 and 1_000_000
    :param annual_interest: a number between 1 and 30
    :param years: A number between 1 and 30
    :return:
    """
    monthly_interest = annual_interest / PERCENT / MONTHS_IN_YEARS
    number_of_payments = years * MONTHS_IN_YEARS

    return (principal
            * (monthly_interest * math.pow(1 + monthly_interest, number_of_payments))
            / (math.pow(1 + monthly_interest, number_of_payments) - 1))


def calculate_balance(principal, annual_interest, years, number_of_payments_made):
    monthly_interest = annual_interest / PERCENT / MONTHS_IN_YEARS
    total_number_of_payments = years * MONTHS_IN_YEARS

    # Correct formula for remaining balance
    numerator = math.pow(1 + monthly_interest, total_number_of_payments) - math.pow(1 + monthly_interest, number_of_payments_made)
    denominator = math.pow(1 + monthly_interest, total_number_of_payments) - 1

    return principal * (numerator / denominator)

def print_mortgage(principal, annual_interest, years):
    mortgage = calculate_mortgage(principal, annual_interest, years)
    print(f"MORTGAGE\n"
          f"------------------------------------------"
          f"Monthly Payments: ${mortgage:.2f}\n")

def print_payment_schedule(principal, annual_interest, years):
    months = years * MONTHS_IN_YEARS
    print(f"PAYMENT SCHEDULE\n"
          f"------------------------------------------")
    for month in range(1, months + 1):
        balance = calculate_balance(principal, annual_interest, years, month)
        print(f"Month {month}:\t ${balance:,.2f}")

def main():
    # Greet the user
    greet_user("John", "Smith")

    principal = read_number("Principal: ",1000,1_000_000)
    annual_interest_rate = read_number("Annual Interest Rate: ",1,30)
    years = read_number("Years: ",1,30)

    print_mortgage(principal, annual_interest_rate, years)
    print_payment_schedule(principal, annual_interest_rate, years)

if __name__ == '__main__':
    main()