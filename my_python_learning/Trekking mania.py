n = int(input())
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []

for i in range (1, n+1):
    gn = int(input())
    if gn <= 5:
        p1.append(gn)
    if 6 <= gn <= 12:
        p2.append(gn)
    if 13 <= gn <= 25:
        p3.append(gn)
    if 26 <= gn <= 40:
        p4.append(gn)
    if gn >= 41:
        p5.append(gn)
total = sum(p1) + sum(p2) + sum(p3) + sum(p4) + sum(p5)

print(f"{(sum(p1) * 100 / total ):.2f}%")
print(f"{(sum(p2) * 100 / total ):.2f}%")
print(f"{(sum(p3) * 100 / total ):.2f}%")
print(f"{(sum(p4) * 100 / total ):.2f}%")
print(f"{(sum(p5) * 100 / total ):.2f}%")
