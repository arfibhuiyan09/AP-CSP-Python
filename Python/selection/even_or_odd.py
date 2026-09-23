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

count = int(input("for how many numbers do you want to find out whether it is even or odd? (INTEGERS ONLY) "))

for i in range(count):
    number = int(input("\nenter ANY random number to determine whether it is even or odd: "))
    if number % 2 == 1:
        message()
        print(f"{number} is a ODD number!\n")
    else:
        message()
        print(f"{number} is a EVEN number!\n")

    count -=1   
    print(f"{count} checks left.")

