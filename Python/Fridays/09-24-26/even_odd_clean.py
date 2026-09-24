# Problem: Given a positive integer, determine if its even or false.

number = int(input())
if number % 2 == 1:
    print("Odd")
elif number % 2 == 0:
    print("Even")