import sys
max_num = -sys.maxsize
sum_num = 0
n = int(input())

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_num += num

if max_num == (sum_num - max_num):
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    sum_num = (sum_num - max_num)
    print(f"Diff = {abs(max_num - sum_num)}")
