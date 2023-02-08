budget = float(input())
gn = int(input())
cn = int(input())
rn = int(input())
gp = 250

gt = gn * gp
cp = 0.35 * gt
ct = cn * cp
rp = 0.1 * gt
rt = rn * rp

bill = gt + ct + rt

if gn > cn:
    bill = 0.85 * bill
if bill <= budget:
    print(f"You have {(budget - bill):.2f} USD left!")
else:
    print(f"Not enough money! You need {(abs(budget - bill)):.2f} USD more!")
