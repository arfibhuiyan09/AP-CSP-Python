# A home air conditioning system calculates the cost of
# running its heating system based on the indoor temperature,
# outdoor temperature, and number of hours the heat operates.

# If the indoor temperature is below 60 degrees,
# the heating system runs at full power, costing $2.50 per hour.
# Otherwise, if the indoor temperature is below 68 degrees
# and the outdoor temperature is below 40 degrees,
# the system runs at reduced power, costing $1.25 per hour.
# Otherwise, the heating system does not run at all.

indoor_temp = float(input("Indoor temperature: "))
outdoor_temp = float(input("Outdoor temperature: "))
hours = float(input("Hours of operation: "))

cost = 0.0

if indoor_temp < 60:
    cost = round(2.5 * hours, 2)

elif indoor_temp < 68 and outdoor_temp < 40:
    cost = round(1.25 * hours, 2)

print(f"you will pay ${cost}")