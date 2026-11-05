# If the visitor is under 5 years old, admission is free.
# Otherwise, if the visitor has a season pass, admission
# is $5.00 regardless of age. 
# Without a season pass,visitors up to age 18 pay $12.00 and adults pay $18.00.

# Locker rental is charged separately based on the number
# of hours used. The first 2 hours cost $3.00 per hour.
# Any time above 2 hours, up to and including 5 hours,
# costs $2.00 per additional hour. Any time above 5 hours
# costs $1.00 per additional hour. Season pass holders
# receive a 50% discount off of the total locker rental price.
# If the visitor is under 5, locker rentals are free of charge.

age = int(input("Visitor age: "))
season_pass = input("Season pass holder (True/False): ") == "True"
hours = int(input("Locker hours needed: "))

total_cost = 0.0

# total_cost

if age < 5:
    total_cost = 0.0
else:
    if season_pass:
        total_cost = 5.00
    else:
        if age < 18: 
            total_cost = 12.00
        else:
            total_cost = 18.00
            
        
# rental costs

if hours < 2:
    total_cost = total_cost * hours
elif 2 < hours <= 5:
    total_cost = total_cost * hours
else:
    total_cost = total_cost * hours
    
if season_pass:
    total_cost /= 2
if age < 5:
    total_cost = 0.00
    
print(total_cost)