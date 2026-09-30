# 09/16/26

# the program takes in an input (grade) and uses if/elif/else statements to select the appropriate response

while True:
    grade = int(input("\nEnter the grade you have for a class currently: "))
    if (grade) > 100:
        print("you somehow got a score above the maximum probably through EC, you absolutely have nothing to worried about right now!")
    elif (grade) >= 90:
        print("Good job! you currently have a A in the class!")
    elif (grade) >= 80:
        print("Good work! you currently have a B in the class!")
    elif (grade) >= 70:
        print("you currently have a C in the class. You might want to bring that up a bit")
    elif (grade) >= 60:
        print(f"you currently have a D... thats not good, attempt to get EC, makeup work, or ANYTHING. You're {grade - 59}% away from an F!")
    else:
        print("you have a F right now. Lock in dude")
