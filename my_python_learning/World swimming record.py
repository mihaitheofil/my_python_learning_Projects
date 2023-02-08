record = float(input())
meters = float(input())
spm = float(input())
resistance = meters // 15 * 12.5
time = meters * spm + resistance
if time < record:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {(time - record):.2f} seconds slower.")
