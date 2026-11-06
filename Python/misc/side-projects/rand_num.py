# 10/04/26

import random
import sys

"""

Random Number Generator/Guessing Game

This script essentially serves two functions: it functions as a Random Number Generator (RNG), or a Random Number Guessing Game.

Users enter into a terminal menu to either 'generate random numbers, or play a random number guessing game', and the choice the user inputs does that function. 

Features:
    - Random Number Generator
    - Random Number Guessing Game
        - Allows On-Demand generation
    - Allows User-Defined Minimum and Maximum bounds
    - Includes a replay system
    - Includes Binary, Bogo, and Linear search algorithms (NEW 10/10/26)

"""

# -------------- CONSTANTS --------------

# ANSI Color codes
GREEN = '\033[32m'

# Text styles
BOLD = '\033[1m'
RESET = '\033[0m'

# -------------- SEARCHING ALGORITHMS --------------

def prompt(num_min, num_max, random_number, count):

    """
    This function serves as the gateway from the manual user-inputted guessing and the algorithmic guessing

    Features:
        - Binary search 
            - The most efficient algorithm in this suite
                - O(log_2(n))
        - Linear search
            - The 2nd most efficient algorithm in this suite
                - O(n)
        - Bogo search
            - The most inefficient algorithm in this suite (and by extension of all time)
                - O(inf)

    """

    done = False

    while True:
        solve = input(f"Do you want to use a searching algorithm to do guess the random number from {num_min} to {num_max}? (y/n) ").lower().strip()

        if solve == "y":
            while True:
                algorithm = input("Which searching algorithm would you like to use? (binary, bogo, linear) ").lower().strip()

                if algorithm == "binary":
                    done = binary_search_algorithm(num_min, num_max, random_number, count)
                    break

                elif algorithm == "linear":
                    done = linear_search_algorithm(num_min, random_number, count)
                    break

                elif algorithm == "bogo":
                    done = bogo_search_algorithm(num_min, num_max, random_number, count)
                    break
                else:
                    print("ERROR: Invalid algorithm choice. Try again!")

        elif solve == "n":
            break

        else:
            print(f"ERROR: '{solve}' was an invalid response. Try again!")

        if done:
            return True

def binary_search_algorithm(num_min, num_max, random_number, count):

    """
    This function consolidates all the calculations for the binary search algorithm.

    How it works:
        - Initializes a count var = 1 and every iteration make it increase by 1
        - the algorithm guesses based on the midpoint of the min and max
        - if statements compare the algorithms guess to the random number
            - Case 1: if bot_guess > random_number: the console will print "lower" and subtract 1 to num_max to create a new midpoint; it is used to shrink the search space after eliminating the middle element.
            - Case 2: if bot_guess < random_number: the console will print "higher" and add 1 to num_min to create a new midpoint and shrink the search---similarly to the other case.
            - Case 3: if bot_guess == random_number the console will print "WON!" with the random number and the number attempts it got it in
                - returns True, signifying that the search has been completed to cascade to the win_status = True selection
    """

    while True:

        count += 1

        bot_guess = num_min + ((num_max - num_min) // 2)

        if bot_guess == random_number: 
            print(f"{BOLD}Congratulations!{RESET} the bot {GREEN}{BOLD}WON!{RESET} They got {random_number} in {count} attempts.\n")
            return True

        elif bot_guess > random_number:
            num_max = bot_guess - 1

        else:
            num_min = bot_guess + 1

        

def bogo_search_algorithm(num_min, num_max, random_number, count):

    """
    This function consolidates all the calculations for the bogo search algorithm.

    How it works:
        - Initializes a count var = 1 and every iteration make it increase by 1
        - the algorithm guesses based on pure randomness (randint(min,max))
        - if statements compare the algorithms guess to the random number
            - Case 1: if bot_guess > random_number: the console will print "lower"
            - Case 2: if bot_guess < random_number: the console will print "higher"

            at the end of Case 1 and 2, the algorithm is going to continously randomise until it gets it.

            - Case 3: if bot_guess == random_number the console will print "WON!" with the random number and the number attempts it got it in
                - returns True, signifying that the search has been completed to cascade to the win_status = True selection
    """

    while True:
        count += 1

        bot_guess = random.randint(num_min, num_max)

        if bot_guess == random_number: 
            print(f"{BOLD}Congratulations!{RESET} the bot {GREEN}{BOLD}WON!{RESET} They got {random_number} in {count} attempts.\n")
            return True

        elif bot_guess > random_number:
            print(f"The random number is {BOLD}lower{RESET} than {bot_guess}") 

        else:
            print(f"The random number is {BOLD}higher{RESET} than {bot_guess}") 


def linear_search_algorithm(num_min, random_number, count):

    """
    This function consolidates all the calculations for the linear search algorithm.
        
    How it works:
        - Initializes a count var = 1 and every iteration make it increase by 1
        - the algorithm guesses starting from the num_min
        - if statements compare the algorithms guess to the random number
            - Case 1: if bot_guess < random_number: the console will print "higher", and adds 1 to bot_guess
            - Case 2: if bot_guess == random_number the console will print "WON!" with the random number and the number attempts it got it in
                - returns True, signifying that the search has been completed to cascade to the win_status = True selection
    """

    bot_guess = num_min

    while True:
        count += 1

        if bot_guess == random_number: 
            print(f"{BOLD}Congratulations!{RESET} the bot {GREEN}{BOLD}WON!{RESET} They got {random_number} in {count} attempts.\n")
            return True

        else:
            bot_guess += 1

# -------------- MAIN PROGRAM LOGIC --------------

def guessing_game():

    """
    The main logic of the human-guessed random number guesser.

    - Includes a dynamic minimum and maximum value that is user-defined
    - Then uses selection to determine if the user value is the random number
        - Case 1: if guess > random_number: the console will print "lower"
        - Case 2: if guess < random_number: the console will print "higher"

        at the end of Case 1 and 2, it will ask the user to reinput a number based on the hint

        - Case 3: if guess == random_number the console will print "WON!" with the random number and the number attempts it got it in
            - returns True, signifying that the guessing has been completed to cascade to the win_status = True selection
    
    """

    num_min = int(input("What is the minimum value you want to guess for? "))
    num_max = int(input("What is the maximum value you want to guess for? "))

    # -------------- CONSTANTS --------------

    random_number = random.randint(num_min,num_max)
    count = 0

    finish = prompt(num_min, num_max, random_number, count)

    if finish:
        return True


    while True:
        guess = int(input(f"\nguess a random number from {num_min} to {num_max}! "))

        if guess > random_number:
            print(f"The random number is {BOLD}lower{RESET} than {guess}") 
        elif guess < random_number:
            print(f"The random number is {BOLD}higher{RESET} than {guess}") 
        
        count += 1

        if guess == random_number:
            print(f"{BOLD}Congratulations!{RESET} you {GREEN}{BOLD}WON!{RESET} You got {random_number} in {count} attempts.\n")
            return True
         

def generator():

        """
        This function serves as the script that generates any number from any user-defined ranges

        Example: num_min = 4, num_max = 100 --> random_number = 64

        This uses a for loop to iterate the script for a user-defined number of times
            - returns True, signifying that the iteration is completed to cascade to the win_status = True selection
        """
        
        number = int(input("How much times do you want to generate random numbers? "))
        num_min = int(input("What is the minimum value for the generator? "))
        num_max = int(input("What is the maximum value for the generator? "))

        for n in range(number):
            print(f"You're random number is {GREEN}{BOLD}{random.randint(num_min,num_max)}{RESET}! Click to proceed to the next number. Amount of numbers left: {(number - 1) - n}\n")
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
