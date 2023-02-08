degrees = int(input())
timeofday = str(input())
outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if timeofday == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif timeofday == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif timeofday == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
if 18 <= degrees <= 24:
    if timeofday == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif timeofday == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif timeofday == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
if degrees >= 25:
    if timeofday == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif timeofday == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif timeofday == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
