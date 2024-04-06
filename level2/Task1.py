# Guessing Game
import random

user_name = input("Please,Enter your Name : ")

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize guess count
    attempts = 0

    
    
    while attempts<10:
        try:
            # Get user's guess
            remaining_attempts = 10-attempts
            print(f"You have {remaining_attempts} remaining Attempts!")
            guess = int(input(f"{user_name}: Guess the number (between 1 and 100): "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! {user_name} you guessed the number {secret_number} correctly in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if secret_number !=guess:
        
        print(f"Nope,The Computer  guessed number was {secret_number}!")

# Run the game

guess_number()
