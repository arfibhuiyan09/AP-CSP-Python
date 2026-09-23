import sys

subtotal = int(input("Subtotal: "))
discount = int(input("Discount: "))
tax_rate = int(input("Tax Rate: "))

if (100 <= subtotal <= 500):
    if (10 <= discount <= 20):
        if (3 <= tax_rate <= 9):
            total = subtotal - discount * (tax_rate/100)
            print(total)
        else:
            sys.exit()
    else:
        sys.exit
else:
    sys.exit()