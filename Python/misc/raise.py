from time import sleep
from sys import exit

choice = int(input("dude you have to be 18+ to use this script dude\n how old are you? "))

if choice < 18:
    err = f"dude get out, your literally {choice}..."
    raise Exception(err)
else:
    print("dude you're not ready for this...")
    for i in range(10, -1, -1):
        print(i)
        sleep(1)
    print("hi")
    sleep(2)
    print("...")
    sleep(0.75)
    print("was that not funny?")
    sleep(1.5)
    print("...")
    sleep(1)
    print("ok ima just die, goodbye...")
    exit()

    
    
