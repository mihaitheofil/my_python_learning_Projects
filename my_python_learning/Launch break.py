series = str(input())
episode = int(input())
period = int(input())
launch = period / 8
rest = period / 4
time_left = period - launch - rest
import math
if episode <= time_left:
    print(f"You have enough time to watch {series} and left with {math.ceil(time_left - episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(episode - time_left)} more minutes.")