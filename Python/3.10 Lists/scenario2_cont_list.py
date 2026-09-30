from random import randint
from time import sleep


def wait():
    print("you wait until AP Score day arrives...")
     
    for i in range(9):
            sleep(1)
            print(f"Week {i+1} passes...\n")

    score = randint(3, 5)

    print("suddenly, your AP Chem score is available to see;")
    sleep(2)
    print(f"you open ap classroom, and see you got a {score}... you were so surprised you had a stroke and went to the ICU in pure joy... \n \n THE END.")

choice_arr = ["", "", "", "", "", ""]
    
print("you are currently taking the Advanced Placement Chemistry exam...")
print("you see 'K' in a FRQ question response,\n")

choice_arr[0] = input("what do you do? (answer/cry/sleep) ").lower().strip()

if choice_arr[0] == "answer":
    print("\nyou tried to answer the question, it read: \n --> CO(g) + 2 H2(g) <=> CH3OH(g)      ΔH = -90 kJ/mol_rxn <--\n \n Given that initially P_CO = 0.50 atm and P_H2 = 1.0 atm, what is the  equilibrium partial pressure of CH3OH if the total pressure in the  container at equilibrium is 0.78 atm?  ")
    choice_arr[1] = float(input("What do you respond with? (WRITE ONLY NUMBER) "))

    if choice_arr[1] == 0.36:
        print(f"You wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... YOU WERE!")

        choice_arr[2] = input("what do you do? (celebrate) ").lower().strip()

        if choice_arr[2] == "celebrate":
            print("you celebrated at the fact you got the question correct miracously; months later you hear that you got a 2 on the exam, causing you to have a stroke\n \n THE END")
     

    elif choice_arr[1] in (0.35, 0.37):
        print(f"You wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... you missed the question within ONE HUNDREDTH... you just faint on the spot at the hearing of this. \n \n THE END")

    else:
        print(f"You wrote {choice_arr[1]} on your test booklet, you later go home to check whether you were right or not and... you were unfortunately wrong...")

        choice_arr[3] = input("what do you do? (sleep/wait) ").lower().strip()

        if choice_arr[3] == "sleep":
                    print("after that question, you go to sleep peacefully not worrying about the exam at all at the moment. You felt at peace \n \n THE END")
        
        if choice_arr[3] == "wait":
            wait()
            
elif choice_arr[0] == "cry":
    print("you cried... thats it... you still failed the question since you didn't bother attempting it :(")

    choice_arr[4] = input("what do you do? (wait) ").lower().strip()

    if choice_arr[4] == "wait":
        wait()

elif choice_arr[0] == "sleep":
    print("you wake up 6 hours later, hours after the AP Exam ended; you failed the question since you didn't attempt it but who knows what you scored on your AP Chem Exam...")

    choice_arr[5] = input("what do you do? (wait) ").lower().strip()
    
    if choice_arr[5] == "wait":
        wait()
