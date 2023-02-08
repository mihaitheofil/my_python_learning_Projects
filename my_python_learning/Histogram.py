import random
n = int(input())
rlist = []
p1list = []
p2list = []
p3list = []
p4list = []
p5list = []

for i in range(1, n+1):
    num = random.randrange(0, 1001)
    rlist.append(num)
    if 1 <= num < 200:
        p1list.append(num)
    elif 200 <= num <= 399:
        p2list.append(num)
    elif 400 <= num <= 599:
        p3list.append(num)
    elif 600 <= num <= 799:
        p4list.append(num)
    else:
        p5list.append(num)

p1 = len(p1list) * 100 / len(rlist)
p2 = len(p2list) * 100 / len(rlist)
p3 = len(p3list) * 100 / len(rlist)
p4 = len(p4list) * 100 / len(rlist)
p5 = len(p5list) * 100 / len(rlist)

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")

