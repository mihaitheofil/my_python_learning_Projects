age = int(input())
wm = float(input())
ptoy = int(input())

money = 0
lost = age // 2

mlist = []
tlist = []

for i in range(1, age+1):
    if i % 2 == 1:
        tlist.append(1)
    if i % 2 == 0:
        money = money + 10
        mlist.append(money)

budget = sum(tlist) * ptoy + sum(mlist) - lost

if budget >= wm:
    print(f"Yes! {(budget - wm):.2f}")
else:
    print(f"No! {(wm - budget):.2f}")
