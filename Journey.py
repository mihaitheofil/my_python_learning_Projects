# A young programmer has an exact budget and free time for each season.
# Write a program that will accept the budget and the season, and print,
# where the programmer will rest and how much he will spend.
# The budget determines the destination, and the season determines
# how much of the budget he will spend. If it is summer, he will rest at the campsite
# and in the winter at a hotel. If he is in Europe, he will stay in a hotel, regardless of the season.
# Each campsite or hotel, according to the destination,
# has its price that corresponds to a certain percentage of the budget:
# ⦁	At 100 USD or less – somewhere in Bulgaria
# ⦁	Summer – 30% of the budget
# ⦁	Winter – 70% of the budget
# ⦁	At 1000 USD or less – somewhere in Bulgaria
# ⦁	Summer – 40% of the budget
# ⦁	Winter – 80% of the budget
# ⦁	For more than 1000 USD. – somewhere in Europe
# ⦁	When travelling in Europe, regardless of the season he will spend 90% of the budget.
# Input Data
# 2 rows are read from the console:
# ⦁	The budget – a floating-point number in the range [10.00...5000.00].
# ⦁	The season – a string "summer" or "winter"
# Output Data
# On the console print.
# ⦁	Somewhere in {destination}
# ⦁	{Type of holiday} – {Money spent}
# ⦁	The Holiday can be a "Camp", or "Hotel"
# ⦁	The amount must be rounded to the second decimal place

# Sample Input and Output

# 	Input	Output

# 50
# summer	Somewhere in Bulgaria
# Camp - 15.00

# 75
# winter	Somewhere in Balkans
# Hotel - 52.50

# 312
# summer	Somewhere in Balkans
# Camp - 124.80

# 678.53
# winter	Somewhere in Balkans
# Hotel - 542.82

# 1500
# summer	Somewhere in Europe
# Hotel - 1350.00

# budget  is [10.00 ... 5000.00]
budget = float(input())
# season is "summer" or "winter"
season = str(input())
destination = ['Bulgaria', 'Balkans', 'Europe']
holiday = ['Hotel', 'Camp']
spent = 0

if budget <= 100:
    destination = destination[0]
    if season == "summer":
        spent = budget * 0.3
        holiday = holiday[1]
    elif season == "winter":
        spent = budget * 0.7
        holiday = holiday[0]
elif 100 < budget <= 1000:
    destination = destination[1]
    if season == "summer":
        spent = budget * 0.4
        holiday = holiday[1]
    elif season == "winter":
        spent = budget * 0.8
        holiday = holiday[0]
elif budget > 1000:
    destination = destination[2]
    holiday = holiday[0]
    spent = budget * 0.9

print(f"Somehere in {destination}")
print(f"{holiday} - {spent:.2f}")