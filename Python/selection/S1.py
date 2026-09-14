age = int(input("yo, how old are you rq? "))

def checkDrivingStatus(age):
    if age >= 18:
        print("oka you are allowed to drive without restrictions, congratulations!")
    elif age >= 15 and age < 18:
        print("oka you are technically allowed to drive but with restrictions. See more at https://www.flhsmv.gov/driver-licenses-id-cards/licensing-requirements-teens-graduated-driver-license-laws-driving-curfews/")
    else:
        print(f"you are legally NOT allowed to drive without a legal guradian present... you still have {18-age} years left tho!")

def checkDrinkStatus(age):
    if age >= 21:
        print("oka you are allowed to drink in the United States of America, drink as you will!")
    else:
        print(f"you can NOT drink right now if you are in the United States of America. Dw, you still have {21-age} years left until you can!")

checkDrivingStatus(age)
checkDrinkStatus(age)