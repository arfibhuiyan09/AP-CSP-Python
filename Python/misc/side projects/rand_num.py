# 10/04/26

import random
import sys

"""

Random Number Generator/Guessing Game

This script essentially serves two fuctions: it functions as a Random Number Generator (RNG), or a Random Number Guessing Game.

Users enter into a terminal menu to either 'generate random numbers, or play a random number guessing game', and the choice the user inputs does that function. 

Features:
    - Random Number Generator
    - Random Number Guessing Game
        - Allows On-Demand generation
    - Allows User-Defined Minimum and Maximum bounds
    - Includes a replay system

"""

# -------------- CONSTANTS --------------

# ANSI Color codes
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'

# Text styles
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALIC = '\033[3m'
RESET = '\033[0m'

def guessing_game():
    min = int(input("What is the minimum value you want to guess for? "))
    max = int(input("What is the maximum value you want to guess for? "))

    # -------------- CONSTANTS --------------
    random_number = random.randint(min,max)
    count = 0

    while True:
        guess = int(input(f"guess a random number from {min} to {max}!"))

        if guess > random_number:
            print(f"The random number is {BOLD}lower{RESET} than {guess}") 
        elif guess < random_number:
            print(f"The random number is {BOLD}higher{RESET} than {guess}") 
        
        count += 1

        if guess == random_number:
            print(f"{BOLD}Congratulations!{RESET} you {GREEN}{BOLD}WON!{RESET} You got {random_number} in {count} attempts.\n")
            return True
         

def generator():
        number = int(input("How much times do you want to generate random numbers? "))
        min = int(input("What is the minimum value for the generator? "))
        max = int(input("What is the maximum value for the generator? "))

        for n in range(number):
            print(f"You're random number is {GREEN}{BOLD}{random.randint(min,max)}{RESET}! Click to proceed to the next number. Amount of numbers left: {(number - 1) - n}\n")
            input()
        return True

while True:
    choice = input("do you want to generate random numbers, or play a random number guessing game? (generator/guess) ").lower().strip()

    if choice == "generator":
        win_status = generator()
    elif choice == "guess":
        win_status = guessing_game()
    else:
        print(f"ERROR: '{choice}' was an invalid response. Try again!")

    if win_status == True:
        while True:
            choice2 = input("Do you want to go back to the menu, or quit? (menu/q) ").lower().strip()

            if choice2 == "menu":
                print()
                break
            elif choice2 == "q":
                print("oka, thanks for playing!")
                sys.exit()
            else:
                print(f"ERROR: '{choice2}' was an invalid response. Try again!")
