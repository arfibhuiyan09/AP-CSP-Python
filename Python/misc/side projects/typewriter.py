import sys
import time

"""

Typewriter Generator:

This script essentially simulates a Typewriter effect by spacing each letter with a list() function, then using a for loop
to iterate through each index with a end="", flush=True to clean the terminal and allow the user to see the live effect.


"""

def effect(word):
    letters = list(word)
    print()
    
    for n in range(len(word)):
        print(letters[n], end="", flush=True) 
        time.sleep(0.075)
    return True

while True:
    word = input("What word do you want to be animated in a typewriter style? ")
    completion_status = effect(word)

    if completion_status: 
        while True:
            choice = input("\n\nDo you want to try again with a different word? (y/n) ").lower().strip()

            if choice in ["y", "yes"]:
                break
            elif choice in ["n", "no"]:
                print("oka")
                sys.exit()
            else:
                print(f"ERROR: '{choice}' was an invalid choice! Try again.")
