# 09/23/26

# the program takes in an input (number) and uses a if/else statement WITH a modulo (%) to see wheter the result is even (0) or odd (1)
# this program also includes an optional 'message' function which just adds personalisation to the code; adding antipication to the result.

from time import sleep

def message():
    print("wait lemme check my databases.")
    sleep(0.5)
    print("wait lemme check my databases..")
    sleep(0.5)
    print("wait lemme check my databases...")
    sleep(0.5)

while True:
    number = int(input("enter ANY random number to determine wheter it is even or odd: "))
    if number % 2 == 1:
        message()
        print(f"{number} is a ODD number!\n")
    elif number % 2 == 0:
        message()
        print(f"{number} is a EVEN number!\n")