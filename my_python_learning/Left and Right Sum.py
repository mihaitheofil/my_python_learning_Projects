n = int(input())
left = 0
right = 0
for i in range (0, n):
    left = left + int(input())
for j in range (0, n):
    right = right + int(input())

if left == right:
    print(f"Yes, sum = {left}")
else:
    print(f"No, diff = {abs(left - right)}")

