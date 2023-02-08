deposit = float(input())
months = int(input())
rate = float(input())
minterest = deposit * rate / 100 / 12
tinterest = months * minterest
amount = deposit + tinterest
print(amount)
