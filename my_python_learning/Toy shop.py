trip = float(input())
np = int(input())
nd = int(input())
nb = int(input())
nm = int(input())
nt = int(input())
p = 2.6
d = 3
b = 4.1
m = 8.2
t = 2
money = p * np + d * nd + b * nb + m * nm + t * nt
if (np + nd + nb + nm + nt) >= 50:
    money = 0.75 * money
money = 0.9 * money
dif = money - trip
if dif >= 0:
    print(f"Yes! {dif:.2f} USD left.")
else:
    print(f"Not enough money! {abs(dif):.2f} USD needed.")
