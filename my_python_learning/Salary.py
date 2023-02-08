n = int(input())
salary = int(input())

for t in range(1, n+1):
    t = str(input())
    if t == "Facebook":
        salary -= 150
    if t == "Instagram":
        salary -= 100
    if t == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)
