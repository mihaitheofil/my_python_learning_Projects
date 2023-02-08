hour = int(input())
d = str(input())
err = 0
mo = 'Monday'
tu = 'Tuesday'
we = 'Wednesday'
th = 'Thursday'
fr = 'Friday'
sa = 'Saturday'
su = 'Sunday'

if hour < 0 or hour > 23:
    err = 1
elif d != mo and d != tu and d != we and d != th and d != fr and d != sa and d != su:
    err = 1
else:
    if 10 <= hour <= 18 and d != "Sunday":
        print("open")
    else:
        print("closed")
if err == 1:
    print("error")
