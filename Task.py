import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    # take input as an lower range 
    lower_bound = int(input("Enter the lower bound of the range: "))
     # take input as an upper range 
    upper_bound = int(input("Enter the upper bound of the range: "))
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts = attempts + 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break

number_guessing_game()