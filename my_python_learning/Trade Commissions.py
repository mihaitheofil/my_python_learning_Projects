town = input()
sales = float(input())
comission = 0

if town == "London" and sales >= 0:
    if 0 <= sales <= 500:
        comission = 0.05
    elif 500 < sales <= 1000:
        comission = 0.07
    elif 1000 < sales <= 10000:
        comission = 0.08
    elif sales > 10000:
        comission = 0.12
    print(f"{(comission * sales):.2f}")

elif town == "Paris" and sales >= 0:
    if 0 <= sales <= 500:
        comission = 0.045
    elif 500 < sales <= 1000:
        comission = 0.075
    elif 1000 < sales <= 10000:
        comission = 0.1
    elif sales > 10000:
        comission = 0.13
    print(f"{(comission * sales):.2f}")

elif town == "Rome" and sales >= 0:
    if 0 <= sales <= 500:
        comission = 0.055
    elif 500 < sales <= 1000:
        comission = 0.08
    elif 1000 < sales <= 10000:
        comission = 0.12
    elif sales > 10000:
        comission = 0.145
    print(f"{(comission * sales):.2f}")

else:
    print("error")