# A water company calculates a customer's monthly bill
# based on the number of gallons of water used.
# The cost is calculated in tiers, so different portions
# of the water usage are charged at different rates.
# The first 1,000 gallons cost $0.02 per gallon. Any usage
# above 1,000 gallons, up to and including 3,000 gallons,
# costs $0.015 per additional gallon. Any usage above
# 3,000 gallons costs $0.01 per additional gallon.

gallons = int(input("Gallons of water used: "))

bill = 0.0

if gallons <= 1000:
    bill = round(0.02 * gallons, 2)

elif 1001 <= gallons <= 3000:
    bill = round(0.015 * gallons, 2)

else:
    bill = round(0.01 * gallons, 2)

print(bill)