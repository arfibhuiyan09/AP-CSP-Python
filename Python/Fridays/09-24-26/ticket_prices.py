# Themeparks are expensive.
# The problem: given a theme park's ticket price, determine whether it is a good deal or not.

price = int(input())

if price == 0:
    print("Free")
elif 1 <= price <= 151:
    print("Cheap")
elif 152 <= price <= 251:
    print("Average")
elif 252 <= price:
    print("Expensive")
