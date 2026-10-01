# 10/01/26 scenario2.py refactored entirely to a full fleged game

import random
import sys
import time

# -------------- FUNCTIONS --------------

# wait helper function to find out AP Scores through `random.randint(a,b)`
def wait():
    print("\nyou wait until AP Score day arrives...")

    for week in range(9):
        time.sleep(0.5)
        print(f"\nWeek {week+1} passes...\n")

    score = random.randint(3, 5)

    print("\nsuddenly, your AP Chem score is available to see;")
    time.sleep(1)
    print(
        f"\nyou open ap classroom, and see you got a {score}... you were so surprised you had a heart attack of pure joy... \n \n THE END (Ending 4)."
    )

# play_again helper function to figure out if the user wants to play again
def play_again():

    while True:
        choice = input("\ndo you want to play again? (Y/N) ").lower().strip()

        if choice in ("y", "yes"):
            print("\noka")
            time.sleep(0.5)

            for i in range(3):
                print(f"\nLoading {'.' * (i+1)}")
                time.sleep(0.5)

            print("\nLoaded!\n\n")
            return  # Returns control to the game loop

        elif choice in ("n", "no"):
            print("\noh oka nws! Thanks for playing!")
            sys.exit()
        else:
            print(
                f"\n'{choice}' is an invalid input! Type your response again please!"
            )

# -------------- BRANCH 1 --------------
def answer():
    print("\nyou tried to answer the question, it read: \n --> CO(g) + 2 H2(g) <=> CH3OH(g)      ΔH = -90 kJ/mol_rxn <--\n \n Given that initially P_CO = 0.50 atm and P_H2 = 1.0 atm, what is the equilibrium partial pressure of CH3OH if the total pressure in the container at equilibrium is 0.78 atm?  ")
    
    # Catch invalid numerical inputs so program doesn't crash on typos
    try:
        ans = round(float(input("\nWhat do you respond with? (WRITE ONLY NUMBER) ")), 2) #literally just rounds a float the user provides to 2 decimal places
        choice_arr.append(ans)
    except ValueError:
        print("\nThat wasn't a valid number! You panicked and left the answer blank.")
        choice_arr.append(0.0)

    # Branch 1a: Correct Answer
    if choice_arr[1] == 0.36:
        print(f"\nYou wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... YOU WERE!")

        cel = input("\nwhat do you do? (celebrate) ").lower().strip()
        choice_arr.append(cel)

        print("\nyou celebrated at the fact you got the question correct miraculously; months later you hear that you got a 2 on the exam, causing you to faint\n \n THE END (Ending 1)")
        return False

    # Branch 1b: Close Miss
    elif choice_arr[1] in (0.35, 0.37):
        print(f"\nYou wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... you missed the question within ONE HUNDREDTH... you just faint on the spot at the hearing of this. \n \n THE END (Ending 2)")
        return False

    # Branch 1c: Incorrect Answer
    else:
        print(f"\nYou wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... you were unfortunately wrong...")

        while True:
            next_move = input("\nwhat do you do? (sleep/wait) ").lower().strip()

            if next_move in ("sleep", "wait"):
                choice_arr.append(next_move)
                break
            else:
                print(f"'{next_move}' is not a option... Choose again.")

        if choice_arr[2] == "sleep":
            print("\nafter that question, you go to sleep peacefully not worrying about the exam at all at the moment. You felt at peace \n \n THE END (Ending 3)")
            return True
        elif choice_arr[2] == "wait":
            wait() # Triggers Ending 4
            return False

# -------------- BRANCH 2 --------------
def cry():

    while True:  # loop until user enters a valid choice
        print("\nyou cried... thats it... you still failed the question since you didn't bother attempting it :(")
        
        cry_move = input("\nwhat do you do? (wait/distract) ").lower().strip()

        if cry_move in ["wait", "distract"]:
            choice_arr.append(cry_move)
            break

        else:
            print(f"'{cry_move}' is not a option... Choose again.")

    # Branch 2a: Waiting until AP Score Day
    if choice_arr[1] == "wait":
        wait()
        return False

    # Branch 2b: Distracting Yourself
    elif choice_arr[1] == "distract":
        print("\nyou try to distract yourself by doing things such as playing videogames, fishing, golfing, just to attempt to forget the horrors of the AP Chemistry exam; it failed.")

        while True:
            reflect = input("\nwhat do you do? (wait) ").lower().strip()

            if reflect == "wait":
                choice_arr.append(reflect)
                break
            else:
                print(f"'{reflect}' is not a option... Choose again.")
                
        wait()
        return False

# -------------- BRANCH 3 --------------
def sleep():

    print("\nyou wake up 6 hours later, hours after the AP Exam ended; you failed the question since you didn't attempt it but who knows what you scored on your AP Chem Exam...")
    
    while True: # loop until user enters a valid choice
        sleep_move = input("\nwhat do you do? (wait/sleep) ").lower().strip()

        if sleep_move in ["wait", "sleep"]:
            choice_arr.append(sleep_move)
            break

        else:
            print(f"'{sleep_move}' is not a option... Choose again.")

    # Branch 3a: Waiting until AP Score Day
    if sleep_move == "wait":
        wait()
        return False

    # Branch 3b: Sleep (again...)
    elif sleep_move == "sleep":
        days = random.randint(50, 100)
        print(f"\nyou slept for ~{days} days, it is currently midnight and you are still at school. You have no clue how to escape, nor what to even do...")

        while True: # nested loop until user enters a valid choice
            midnight_move = input("\nby what method do you attempt to escape with? (door/windows/roof/front_office) ").lower().strip()

            if midnight_move in ["door", "windows", "roof", "front_office"]:
                choice_arr.append(midnight_move)
                break
            
            else:
                print(f"'{midnight_move}' is not a option... Choose again.")

        # Branch 3bi: Escaping the school via door
        if midnight_move == "door":
            print("\nyou attempt to escape by busting the door open, but it was to no avail...\n")
            return False

        # Branch 3bii: Escaping the school via windows
        elif midnight_move == "windows":
            print("\nyou found a random window in the stairwell of the school...")

            while True: # nested, nested loop until user enters a valid choice
                item = input("\nwhat do you throw to break it? (chair/rock/pencil/paper_airplane) ").lower().strip()

                if item in ["chair", "rock", "pencil", "paper_airplane"]:
                    choice_arr.append(item)
                    break

                else:
                    print(f"'{item}' is not a option... Choose again.")

            # Branch 3biiA: Throwing a chair at the window
            if item == "chair":
                print(f"\nyou threw the {item}, but it didn't break the window? You were surprised.\n")
                return False

            # Branch 3biiB: Throwing a rock at the window
            elif item == "rock":
                print(f"\nyou threw the {item}, (and unsurprisingly) broke the window!")
                print("\nyou were able to escape the school and go home safely! \n \n THE END (Ending 5)")
                return True

            # Branch 3biiC: Throwing a pencil/paper plane at the window
            elif item in ["pencil", "paper_airplane"]:
                print(f"\nyou threw {item}, but it just reflected from the window...\n")
                return False

        # Branch 3biii: Escaping the school via roof/front office
        elif midnight_move in ["roof", "front_office"]:
            print(f"\nyou checked the {midnight_move}, but it was locked...\n")
            return False

# ---------MAIN GAME LOOP-----------
def main():
    print("you are currently taking the Advanced Placement Chemistry exam...")
    print("you see 'K' in a FRQ question response,\n")

    while True: # initial while loop to validate actions
        action = input("\nwhat do you do? (answer/cry/sleep) ").lower().strip()
        if action in ["answer", "cry", "sleep"]:
            choice_arr.append(action)
            break
            
        print(f"'{action}' is not a option... Choose again.")

# introduction / one time use code
while True:

    choice = input("Hey! Before you play this AP Chemistry-inspired text-adventure, do you want to read a tutorial? or to start the game? (tutorial/play) ").lower().strip()

    if choice in ("tut", "tutorial"):
        # ANSI Color codes
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        CYAN = '\033[36m'
        MAGENTA = '\033[35m'

        # Text styles
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

        print(f"Alright so, the {GREEN}{UNDERLINE}goal{RESET} of this text adventure is to survive the aftermath of an AP Chemistry exam and discover one of five possible endings\n")
        time.sleep(2)
        print("You will be placed in a scenario where you have just taken an AP Chemistry exam.\n")
        time.sleep(2)
        print(f"When prompted, type one of the available options, such as {RED}'answer'{RESET}, {GREEN}'cry'{RESET}, and {CYAN}'sleep'{RESET}.\n")
        time.sleep(2)
        print(f"If the game lists specific options, {BOLD}{UNDERLINE}enter one of those options to continue.{RESET}\n")
        time.sleep(2)
        print("Your choices determine which of the five endings you reach.\n")
        time.sleep(2)
        print(f"When the game asks whether you want to play again, enter {BOLD}Y{RESET} to restart or {BOLD}N{RESET} to quit.\n")
        print(f"Thats it! In a few seconds you could choose whether to repeat this tutorial or to start the game, {GREEN}{BOLD}{UNDERLINE}Good Luck!{RESET}\n")
        time.sleep(2)


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
                winStatus = "(WIN)"
            else:
                winStatus = "(LOSE)"
                
            # game summary
            print("\n--------------------------------------------------")
            print(f"GAME OVER {winStatus} - SUMMARY OF YOUR VALID CHOICES:")
            print(choice_arr)
            print("--------------------------------------------------")

            # single call to play_again() at the end of every branch
            play_again()

    else:
        print(f"'{choice}' is not a option... Choose again.")
        break