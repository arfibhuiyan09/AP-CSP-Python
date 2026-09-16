# 09/16/26

# The program takes in an input (age) and uses if/elif/else statements to print 1 line determining wheter they can drive, vote, and drink. 
# the if/elif statements for ages 16<=x<21 uses the "and" operator to establish a range of valid inputs where the program could activate.

age = int(input("yo, how old are you rq? "))

if age >= 16 and age < 18:
    print("you are able to drive (with restrictions) but can't vote in the United States nor drink.")
elif age >= 18 and age < 21:
    print("you are able to drive and vote in the United States but you can't drink.")
elif age >= 21:
    print("you are able to drink, vote, and drink in the United States!")
else:
    print("you are NOT to drive, vote, nor drink in the United States...")