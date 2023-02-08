n = int(input())
odds = 0
evens = 0

for i in range (1, n+1):
    num = int(input())
    if i % 2 ==0:
        evens += num
    else:
        odds += num

if evens == odds:
    print("Yes")
    print(f"Sum = {evens}")
else:
    print("No")
    print(f"Diff = {abs(evens-odds)}")