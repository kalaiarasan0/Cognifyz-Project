#Number Guesser
import random

def guess_number(minimum, maximum):
    # Generate a random number within the specified range
    first_gen_number = random.randint(minimum, maximum)
    second_gen_number = random.randint(minimum, maximum)
    add_gen_number = first_gen_number + second_gen_number
    round_off_gen_number = round(add_gen_number/2)

    secret_number = round_off_gen_number
    
    
    print(f"Welcome to the Number Guessing Game! Guess a number between {minimum} and {maximum}.")
    print("Keep in mind you have 15 Attempts Only!")

    attempts = 0
    
    while attempts<10:
        try:
            # Get user's guess
            
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if secret_number != guess:
        print(f"Nope,The Computer guessed number was {secret_number}!")

# Define the range for the game
minimum = int(input("Please Enter Minimum value:"))
maximum = int(input("Please Enter Maximum value:"))

# Run the game
guess_number(minimum, maximum)
