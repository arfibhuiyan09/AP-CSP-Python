# 09/30/26 scenario2 + loop + lists + nested if-else

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

    print("")
    while True:
        choice = input("\ndo you want to play again? (Y/N) ").lower().strip()

        if choice in ("y", "yes"):
            print("\noka")
            time.sleep(0.5)

            for i in range(3):
                print(f"\nLoading {'.' * (i+1)}")
                time.sleep(0.5)

            print("\nLoaded!\n\n")
            return  # Returns to outer main loop cleanly

        elif choice in ("n", "no"):
            print("\noh oka nws! Thanks for playing!")
            sys.exit()
        else:
            print(
                f"\n'{choice}' is an invalid input! Type your response again please!"
            )


# Main Game Loop

choice_arr = []

while True:
    action = input("\nwhat do you do? (answer/cry/sleep) ").lower().strip()
    if action in ["answer", "cry", "sleep"]:
        choice_arr.append(action)
        break
        
    print(f"'{action}' is not a option... Choose again.")

# -------------- BRANCH 1 --------------

if choice_arr[0] == "answer":
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

    # Branch 1b: Close Miss
    elif choice_arr[1] in (0.35, 0.37):
        print(f"\nYou wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... you missed the question within ONE HUNDREDTH... you just faint on the spot at the hearing of this. \n \n THE END (Ending 2)")

    # Branch 1c: Incorrect Answer
    else:
        print(f"\nYou wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... you were unfortunately wrong...")

        next_move = input("\nwhat do you do? (sleep/wait) ").lower().strip()
        choice_arr.append(next_move)

        if choice_arr[2] == "sleep":
            print("\nafter that question, you go to sleep peacefully not worrying about the exam at all at the moment. You felt at peace \n \n THE END (Ending 3)")
        elif choice_arr[2] == "wait":
            wait() # Triggers Ending 4

# -------------- BRANCH 2 --------------

# Branch 2: Cry
elif choice_arr[0] == "cry":
    while True:
        print("\nyou cried... thats it... you still failed the question since you didn't bother attempting it :(")

        cry_move = input("\nwhat do you do? (wait/distract) ").lower().strip()
        choice_arr.append(cry_move)

        # Branch 2a: Waiting until AP Score Day
        if choice_arr[1] == "wait":
            wait()

        # Branch 2b: Distracting Yourself
        elif choice_arr[1] == "distract":
            print("\nyou try to distract yourself by doing things such as playing videogames, fishing, golfing, just to attempt to forget the horrors of the AP Chemistry exam; it failed.")
            reflect = input("\nwhat do you do? (wait) ").lower().strip()
            choice_arr.append(reflect)
            wait()

        else:
            print(f"'{cry_move}' is not a option... Choose again.")

# -------------- BRANCH 3 --------------

# Branch 3: Sleep
elif choice_arr[0] == "sleep":
    print("\nyou wake up 6 hours later, hours after the AP Exam ended; you failed the question since you didn't attempt it but who knows what you scored on your AP Chem Exam...")

    while True:
        sleep_move = input("\nwhat do you do? (wait/sleep) ").lower().strip()
        choice_arr.append(sleep_move)

        # Branch 3a: Waiting until AP Score Day
        if sleep_move == "wait":
            wait()

        # Branch 3b: Sleep (again...)
        elif sleep_move == "sleep":
            days = random.randint(50, 100)
            print(f"\nyou slept for ~{days} days, it is currently midnight and you are still at school. You have no clue how to escape, nor what to even do...")

            while True:
                midnight_move = input("\nby what method do you attempt to escape with? (door/windows/roof/front_office) ").lower().strip()
                choice_arr.append(midnight_move)

                # Branch 3bi: Escaping the school via door
                if midnight_move == "door":
                    print("\nyou attempt to escape by busting the door open, but it was to no avail...\n")

                # Branch 3bii: Escaping the school via windows
                elif midnight_move == "windows":
                    print("\nyou found a random window in the stairwell of the school...")

                    while True:
                        item = input("\nwhat do you throw to break it? (chair/rock/pencil/paper_airplane) ").lower().strip()
                        choice_arr.append(item)

                        # Branch 3biiA: Throwing a chair at the window
                        if item == "chair":
                            print(f"\nyou threw the {item}, but it didn't break the window? You were surprised.\n")

                        # Branch 3biiB: Throwing a rock at the window
                        elif item == "rock":
                            print(f"\nyou threw the {item}, (and unsurprisingly) broke the window!")
                            print("\nyou were able to escape the school and go home safely! \n \n THE END (Ending 5)")
                            break

                        # Branch 3biiC: Throwing a pencil/paper plane at the window
                        elif item in ["pencil", "paper_airplane"]:
                            print(f"\nyou threw {item}, but it just reflected from the window...\n")

                    break

                # Branch 3biii: Escaping the school via roof/front office
                elif midnight_move in ["roof", "front_office"]:
                    print(f"\nyou checked the {midnight_move}, but it was locked...\n")
                
                else:
                    print(f"'{midnight_move}' is not a option... Choose again.")
        else:
            print(f"'{sleep_move}' is not a option... Choose again.")

        
else:
    print("\nInvalid choice! You stood there frozen and ran out of time. \n \n THE END (Ending 6)")

    
# game summary
print("\n--------------------------------------------------")
print("GAME OVER - SUMMARY OF YOUR VALID CHOICES:")
print(choice_arr)
print("--------------------------------------------------")

# single call to play_again() at the end of every branch
play_again()