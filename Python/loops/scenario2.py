print("you are currently taking the Advanced Placement Chemistry exam...")
print("you see 'K' in a FRQ question response,\n")

choice = input("what do you do? (answer/cry/sleep) ").lower().strip()

while True:

    if choice == "answer":
        print("you tried to answer the question, but after you were told to  Write the expression for the equilibrium constant, K_p, for the reaction, you wrote '2', and got it wrong...")
        break
    elif choice == "cry":
        print("you cried... thats it... you still failed the question since you didn't bother attempting it :(")
        break
    elif choice == "sleep":
        print("you wake up 6 hours later, hours after the AP Exam ended, you failed the question since you didn't attempt it but who knows what you scored on your AP Chem Exam...")
        break


# while choice not in {"answer", "cry", "sleep"}:

# while choice != "answer" and choice != "cry" and choice != "sleep":