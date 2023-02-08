pages_book = int(input())
pages_hour = int(input())
due_days = int(input())
pages_dayly = pages_book / due_days
hours = pages_dayly // pages_hour
print(hours)