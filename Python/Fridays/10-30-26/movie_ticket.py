# A movie theater calculates ticket prices based on the
# customer's age and the day of the week. If the customer
# is under 13 years old, the ticket costs $6.00. If the
# customer is at least 65 years old, the ticket costs $7.00.
# Otherwise, if it is a weekday (Monday through Friday),
# the ticket costs $10.00. Otherwise, the ticket costs $13.00.

age = int(input("Customer age: "))
weekday = input("Day of the week: ")

price = 0.0

if age < 13:
    price = 6
elif age > 65:
    price = 7
elif weekday in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    price = 10
else:
    price = 13


print(price)