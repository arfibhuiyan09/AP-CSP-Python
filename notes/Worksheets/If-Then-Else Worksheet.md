# If-Then-Else worksheet 09/18/26

#### Question: Sort the following into 10 distinct if-then-else blocks then code 3 examples yourself.

1) If the traffic light is red, stop the car; else, keep driving.
2) If the water bottle is empty, fill it up; else, drink from it.
3) If the door is locked, use the key; else, open the door.
4) If the teacher is absent, finish the busy work; else, listen to the lecture.
5) If the cell phone is out of battery, charge it; else, make a call.
6) If the bus arrives before the train, take the bus; else, take the train.
7) If the alarm clock rings, wake up; else, keep sleeping.
8) If the shirt is clean, put it in the closet; else, put it in the laundry basket.
9) If the resturant is crowded, put your name on the waiting list; else, ask for a table.
10) If it is cloudy outside, bring an umbrella; else, wear sunglasses.

### custom if-then-else code number 1 (grade calc):
```py
    print("give 5 grades (in %) to avg")
    g1 = float(input("Grade 1:"))
    g2 = float(input("Grade 2:"))
    g3 = float(input("Grade 3:"))
    g4 = float(input("Grade 4:"))
    g5 = float(input("Grade 5:"))

    total = (g1+g2+g3+g4+g5)/5
    print(total)

    if total > 90:
        print("that results in a A")
    elif total >= 80:
        print("that results in a B")
    elif total >= 70:
        print("that results in a C")
    elif total >= 60:
        print("that results in a D")
    else: 
        print("that results in a F")
```

### custom if-then-else code number 2 (random number guesser):
```py
    while not win:
    choice = input("want to play number game (Y/N) ").lower().strip()
    if choice == "y":
        number = random.randint(min,max)
        while True:
            guess = int(input(f"oka guess a random number from a 1-1000. You have {attempts} attempts left "))
            if guess > number:
                print(f"{guess} is too high!")
                attempts -=1
                count +=1
            elif guess < number:
                print(f"{guess} is too low!")
                attempts -=1
                count +=1
            elif guess == number:
                print(f"GGs, the answer was {number}. you got the answer in {count}/7 total attempts!")
                win = True
                break
            elif attempts == 0:
                print("You have ran out of attempts...")
                break
            else:
                print(f" {choice} was a invalid prompt, try again!")
```
### custom if-then-else code number 3 (code snippet of a ROBLOX JToH/EToH tower guesser script):
```py
    def playquiz():
                    
            if acronymct < TOWER_ACRONYM_COUNT:
                timer()
                incorrect_sfx.play()
                print(f"it has more chars than {acronymct} ⬆️\n")
            elif acronymct > TOWER_ACRONYM_COUNT:
                print(f"it has less chars than {acronymct} ⬇️\n")
                timer()
                incorrect_sfx.play()
            elif acronymct == TOWER_ACRONYM_COUNT:
                timer()
                correct_sfx.play()
                print(f"it has {acronymct} chars 🟩\n")

            time.sleep(1) #delay
        
            if difficulty < TOWER_DIFFICULTY:
                timer()
                incorrect_sfx.play()
                print(f"it is harder than {converted_difficulty} ⬆️\n")
            elif difficulty > TOWER_DIFFICULTY:
                timer()
                incorrect_sfx.play()
                print(f"it is easier than {converted_difficulty} ⬇️\n")
            elif difficulty == TOWER_DIFFICULTY:
                timer()
                correct_sfx.play()
                print(f"it is {converted_difficulty} 🟩\n")

                
            time.sleep(1) #delay

            if towertype != ACTUAL_TOWER_TYPE:
                timer()
                incorrect_sfx.play()
                print(f"it is not {converted_type} ❌\n")

            elif towertype == ACTUAL_TOWER_TYPE:
                timer()
                correct_sfx.play()
                print(f"it is a {converted_type} 🟩\n")

            time.sleep(1.5) #delay

            lives -= 3
            
            if acronymct == TOWER_ACRONYM_COUNT and difficulty == TOWER_DIFFICULTY and towertype == ACTUAL_TOWER_TYPE:
                print("you got the right combination!")
                tower_guess = input("now you have one chance to get the tower. Enter the acronym of the tower. If you don't get it, you lose.  ").lower().strip()

                if tower_guess != ACTUAL_TOWER:
                    timer()
                    womp_womp_sfx.play()
                    print(f"So close, the tower was {ACTUAL_TOWER}.")
                    time.sleep(4) #let the audio of the user's failures play fully
                    sys.exit()
                elif tower_guess == ACTUAL_TOWER:
                    timer()
                    the_boreen_sfx.play()
                    print(f"Good Job! you got the tower name right. It was {ACTUAL_TOWER}!")
                    time.sleep(48) #let the audio of the user's success play fully
                    sys.exit()

        while win:
            actual_lives = lives // 3 
            print(f"you have {actual_lives} lives currently.")
            if lives <= 0:
                womp_womp_sfx.play()
                print("You ran out of lives. Goodbye.")
                time.sleep(4) #let the audio of the user's failures play fully
                sys.exit()
            print(f"Current Date: {date.today()}")
```

### 3 sequence based if-then-else statements:

`If Samuel De Jesus got a 5 on AP Chemistry, he will be flabergasted; else, he will be unphased.`

`If the duck is green, it is not a goose; else, it is a duck.`

`If Azizur never left Kissimmee Middle School in 6th grade to go to OSCS in 7th, he would have done on-level academics; else, he would've done the highest level of academic rigor.`