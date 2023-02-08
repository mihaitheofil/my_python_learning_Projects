import math
hour = int(input())
minutes = int(input())
time = hour * 60 + minutes + 15
nhour = math.floor(time / 60)
nmins = time % 60
if nhour >= 24:
    nhour = nhour % 24
if nmins < 9:
    print(f"{nhour}:0{nmins}")
else:
    print(f"{nhour}:{nmins}")


