#experimentation with `match`

# 4 func calc (09/26/26)


def setup(choice):
    print(f"choose two numbers to {choice}")
    try:
        num1 = float(input("number 1:  "))
        num2 = float(input("number 2:  "))
        return num1, num2
    except ValueError:
        print("ERROR 460: Forbidden characters entered. Try again.")
        return None

def add(choice):
    values = setup(choice)

    if values is None:
        return

    num1, num2 = values
    total_add = (num1 + num2)
    print(f"the answer is {round(total_add, 3)}")

def subtract(choice):
    values = setup(choice)
    
    if values is None:
            return
    
    num1, num2 = values
    total_sub = (num1 - num2)
    print(f"the answer is {round(total_sub, 3)}")

def multiply(choice):
    values = setup(choice)
        
    if values is None:
        return
        
    num1, num2 = values
    total_mul = (num1 * num2)
    print(f"the answer is {round(total_mul, 3)}")

def divide(choice):
    try:
        values = setup(choice)
                
        if values is None:
                return
                
        num1, num2 = values
        total_div = (num1 / num2)
        print(f"the answer is {round(total_div, 3)}")
    except ZeroDivisionError:
        print(f"ERROR 200: {num1} / {num2} is not allowed; you can not divide by zero. Try again.")

while True:
    choice = input("\ndo you want to add, subtract, multiply, divide, or quit? ").lower()

    match choice:
        case "add":
            add(choice)
        case "subtract":
            subtract(choice)
        case "multiply":
            multiply(choice)
        case "divide":
            divide(choice)
        case "quit":
            break
        case _:
            print("Invalid response, try again!\n")