import math

n = int(input())
ranking = int(input())

wlist = []
flist = []
sflist = []

for i in range (1,n+1):
    stage = str(input())
    if stage == "W":
        ranking += 2000
        wlist.append(1)
    if stage == "F":
        ranking += 1200
        flist.append(1)
    if stage == "SF":
        ranking += 720
        sflist.append(1)

avepoints = (len(wlist) * 2000 + len(flist) * 1200 + len(sflist) * 720) / n

print(f"Final points: {ranking}")
print(f"Average points: {math.floor(avepoints)}")
print(f"{(len(wlist) * 100 / n):.2f}%")