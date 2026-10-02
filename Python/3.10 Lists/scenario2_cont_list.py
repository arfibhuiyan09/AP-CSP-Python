# 10/01/26 scenario2.py refactored entirely to a full fleged game

import random
import sys
import time

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

# -------------- FUNCTIONS --------------

# wait helper function to find out AP Scores through `random.randint(a,b)`
def wait():
    print("\nyou wait until AP Score day arrives...")

    for week in range(9):
        time.sleep(0.5)
        print(f"\nWeek {YELLOW}{week+1}{RESET} passes...\n")

    score = random.randint(3, 5)

    print("\nsuddenly, your AP Chem score is available to see;")
    time.sleep(1)
    print(
        f"\nyou open ap classroom, and see you got a {GREEN}{BOLD}{score}{RESET}... you were so surprised you had a heart attack of pure joy... \n \n {BOLD}{RED}THE END{RESET} (Ending 4)."
    )

# play_again helper function to figure out if the user wants to play again
def play_again():

    while True:
        choice = input(f"\ndo you want to play again? ({GREEN}Y{RESET}/{RED}N{RESET}) ").lower().strip()

        if choice in ("y", "yes"):
            print("\noka")
            time.sleep(0.5)

            for i in range(3):
                print(f"\nLoading .")
                time.sleep(0.5)

            print(f"\n{GREEN}{BOLD}Loaded!{RESET}\n\n")
            return  # Returns control to the game loop

        elif choice in ("n", "no"):
            print("\noh oka nws! Thanks for playing!")
            sys.exit()

        else:
            print(f"\n'{RED}{choice}{RESET}' is an invalid input! Type your response again please!")

# -------------- BRANCH 1 --------------
def answer():
    print(f"\nyou tried to answer the question, it read: \n --> {YELLOW}{BOLD}CO(g) + 2 H2(g) <=> CH3OH(g)    ΔH = -90 kJ/mol_rxn{RESET} <--\n \n Given that initially {YELLOW}P_CO = 0.50 atm{RESET} and {YELLOW}P_H2 = 1.0 atm{RESET}, what is the equilibrium partial pressure of CH3OH if the total pressure in the container at equilibrium is {YELLOW}0.78 atm?{RESET}  ")
    
    # Catch invalid numerical inputs so program doesn't crash on typos
    try:
        ans = round(float(input(f"\nWhat do you respond with? ({YELLOW}WRITE ONLY NUMBER{RESET}) ")), 2) # rounds input float to 2 decimal places
        choice_arr.append(ans)
    except ValueError:
        print(f"\nThat wasn't a valid number! You panicked and left the answer blank.")
        choice_arr.append(0.0)

    # Branch 1a: Correct Answer
    if choice_arr[1] == 0.36:
        print(f"\nYou wrote {YELLOW}{choice_arr[1]}{RESET} on your test booklet, you later go home to check whether you were right or not and... YOU WERE RIGHT!")

        while True:
            cel = input(f"\nwhat do you do? ({GREEN}celebrate{RESET}) ").lower().strip()

            if cel == "celebrate":
                choice_arr.append(cel)
                break
            else:
                print(f"'{RED}{cel}{RESET}' is not an option... Choose again.")

        score = random.randint(1, 2)

        print(f"\nyou celebrated at the fact you got the question correct miraculously; months later you hear that you got a {RED}{BOLD}{score}{RESET} on the exam, causing you to faint\n \n {BOLD}{RED}THE END{RESET} (Ending 1)")
        return False

    # Branch 1b: Close Miss
    elif choice_arr[1] in (0.35, 0.37):
        print(f"\nYou wrote {YELLOW}{choice_arr[1]}{RESET} on your test booklet, you later go home to check whether you were right or not and... you missed the question within ONE HUNDREDTH... you just faint on the spot at the hearing of this. \n \n {BOLD}{RED}THE END{RESET} (Ending 2)")
        return False

    # Branch 1c: Incorrect Answer
    else:
        print(f"\nYou wrote {YELLOW}{choice_arr[1]}{RESET} on your test booklet, you later go home to check whether you were right or not and... you were unfortunately wrong...")

        while True:
            next_move = input(f"\nwhat do you do? ({GREEN}sleep{RESET}/{YELLOW}wait{RESET}) ").lower().strip()

            if next_move in ("sleep", "wait"):
                choice_arr.append(next_move)
                break
            else:
                print(f"'{RED}{next_move}{RESET}' is not an option... Choose again.")

        if choice_arr[2] == "sleep":
            print(f"\nafter that question, you go to sleep peacefully not worrying about the exam at all at the moment. You felt at peace \n \n {BOLD}{RED}THE END{RESET} (Ending 3)")
            return True
        elif choice_arr[2] == "wait":
            wait() # Triggers Ending 4
            return False

# -------------- BRANCH 2 --------------
def cry():

    while True:  # loop until user enters a valid choice
        print("\nyou cried... thats it... you still failed the question since you didn't bother attempting it :(")
        
        cry_move = input(f"\nwhat do you do? ({YELLOW}wait{RESET}/{GREEN}distract{RESET}) ").lower().strip()

        if cry_move in ["wait", "distract"]:
            choice_arr.append(cry_move)
            break

        else:
            print(f"'{RED}{cry_move}{RESET}' is not an option... Choose again.")

    # Branch 2a: Waiting until AP Score Day
    if choice_arr[1] == "wait":
        wait()
        return False

    # Branch 2b: Distracting Yourself
    elif choice_arr[1] == "distract":
        print("\nyou try to distract yourself by doing things such as playing videogames, fishing, golfing, just to attempt to forget the horrors of the AP Chemistry exam; it failed.")

        while True:
            reflect = input(f"\nwhat do you do? ({YELLOW}wait{RESET}) ").lower().strip()

            if reflect == "wait":
                choice_arr.append(reflect)
                break
            else:
                print(f"'{RED}{reflect}{RESET}' is not an option... Choose again.")
                
        wait()
        return False

# -------------- BRANCH 3 --------------
def sleep():

    print("\nyou wake up 6 hours later, hours after the AP Exam ended; you failed the question since you didn't attempt it but who knows what you scored on your AP Chem Exam...")
    
    while True: # loop until user enters a valid choice
        sleep_move = input(f"\nwhat do you do? ({YELLOW}wait{RESET}/{GREEN}sleep{RESET}) ").lower().strip()

        if sleep_move in ["wait", "sleep"]:
            choice_arr.append(sleep_move)
            break

        else:
            print(f"'{RED}{sleep_move}{RESET}' is not an option... Choose again.")

    # Branch 3a: Waiting until AP Score Day
    if sleep_move == "wait":
        wait()
        return False

    # Branch 3b: Sleep (again...)
    elif sleep_move == "sleep":
        days = random.randint(50, 100)
        print(f"\nyou slept for ~{YELLOW}{days}{RESET} days, it is currently midnight and you are still at school. You have no clue how to escape, nor what to even do...")

        while True: # nested loop until user enters a valid choice
            midnight_move = input(f"\nby what method do you attempt to escape with? ({GREEN}door{RESET}/{YELLOW}windows{RESET}/{RED}roof{RESET}/{GREEN}front_office{RESET}) ").lower().strip()

            if midnight_move in ["door", "windows", "roof", "front_office"]:
                choice_arr.append(midnight_move)
                break
            
            else:
                print(f"'{RED}{midnight_move}{RESET}' is not an option... Choose again.")

        # Branch 3bi: Escaping the school via door
        if midnight_move == "door":
            print("\nyou attempt to escape by busting the door open, but it was to no avail...\n")
            return False

        # Branch 3bii: Escaping the school via windows
        elif midnight_move == "windows":
            print("\nyou found a random window in the stairwell of the school...")

            while True: # nested, nested loop until user enters a valid choice
                item = input(f"\nwhat do you throw to break it? ({GREEN}chair{RESET}/{YELLOW}rock{RESET}/{RED}pencil{RESET}/{GREEN}paper_airplane{RESET}) ").lower().strip()

                if item in ["chair", "rock", "pencil", "paper_airplane"]:
                    choice_arr.append(item)
                    break

                else:
                    print(f"'{RED}{item}{RESET}' is not an option... Choose again.")

            # Branch 3biiA: Throwing a chair at the window
            if item == "chair":
                print(f"\nyou threw the {YELLOW}{item}{RESET}, but it didn't break the window? You were surprised.\n")
                return False

            # Branch 3biiB: Throwing a rock at the window
            elif item == "rock":
                print(f"\nyou threw the {YELLOW}{item}{RESET}, (and unsurprisingly) broke the window!")
                print(f"\nyou were able to escape the school and go home safely! \n \n {BOLD}{RED}THE END{RESET} (Ending 5)")
                return True

            # Branch 3biiC: Throwing a pencil/paper plane at the window
            elif item in ["pencil", "paper_airplane"]:
                print(f"\nyou threw {YELLOW}{item}{RESET}, but it just reflected from the window...\n")
                return False

        # Branch 3biii: Escaping the school via roof/front office
        elif midnight_move in ["roof", "front_office"]:
            print(f"\nyou checked the {YELLOW}{midnight_move}{RESET}, but it was locked...\n")
            return False

# ---------MAIN GAME LOOP-----------
def main():
    print("you are currently taking the Advanced Placement Chemistry exam...")
    print("you see 'K' in a FRQ question response,\n")

    while True: # initial while loop to validate actions
        action = input(f"\nwhat do you do? ({GREEN}answer{RESET}/{YELLOW}cry{RESET}/{RED}sleep{RESET}) ").lower().strip()
        if action in ["answer", "cry", "sleep"]:
            choice_arr.append(action)
            break
            
        print(f"'{RED}{action}{RESET}' is not an option... Choose again.")

# introduction / one time use code
while True:

    choice = input(f"Hey! Before you play this AP Chemistry-inspired text-adventure, do you want to read a tutorial? or to start the game? ({YELLOW}tutorial{RESET}/{GREEN}play{RESET}) ").lower().strip()

    if choice in ("tut", "tutorial"):

        print(f"\nAlright so, the goal of this text adventure is to survive the aftermath of an AP Chemistry exam and discover one of five possible endings\n")
        time.sleep(2)
        print("You will be placed in a scenario where you have just taken an AP Chemistry exam.\n")
        time.sleep(2)
        print(f"When prompted, type one of the available options, such as {GREEN}'answer'{RESET}, {YELLOW}'cry'{RESET}, and {RED}'sleep'{RESET}.\n")
        time.sleep(2)
        print("If the game lists specific options, enter one of those options to continue.\n")
        time.sleep(2)
        print("Your choices determine which of the five endings you reach.\n")
        time.sleep(2)
        print(f"When the game asks whether you want to play again, enter {GREEN}Y{RESET} to restart or {RED}N{RESET} to quit.\n")
        print(f"Thats it! In a few seconds you could choose whether to repeat this tutorial or to start the game, {GREEN}{BOLD}Good Luck!{RESET}\n")
        time.sleep(3)

    elif choice == "play":
        print() 

        while True:
            choice_arr = []

            main()

            # Branch 1: Answer
            if choice_arr[0] == "answer":
                win = answer()

            # Branch 2: Cry
            elif choice_arr[0] == "cry":
                win = cry()

            # Branch 3: Sleep
            elif choice_arr[0] == "sleep":
                win = sleep()

            # check if the user 'won, or not
            if win:
                winStatus = f"{GREEN}(WIN){RESET}"
            else:
                winStatus = f"{RED}(LOSE){RESET}"
                
            # game summary
            print("\n--------------------------------------------------")
            print(f"GAME OVER {winStatus} SUMMARY OF YOUR VALID CHOICES:")
            print(choice_arr)
            print("--------------------------------------------------")

            # single call to play_again() at the end of every branch
            play_again()

    else:
        print(f"'{RED}{choice}{RESET}' is not an option... Choose again.")