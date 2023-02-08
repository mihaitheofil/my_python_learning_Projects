budget = float(input())
extras = int(input())
clothing = float(input())
decor = 0.10 * budget
clothes = extras * clothing
if extras >= 150:
    clothes = 0.90 * clothes
sum = decor + clothes
if sum <= budget:
    print("Action!")
    print(f"Wingard starts filming with {(budget - sum):.2f} USD left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs((budget - sum)):.2f} USD more.")
