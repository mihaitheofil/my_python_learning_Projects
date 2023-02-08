a = str(input())
p = float(input())
n = int(input())

for i in range (1, n + 1):
    asn = str(input())
    ass = float(input())
    p += len(asn) * ass / 2
    if p >= 1250.5:
        print(f"Congratulations, {a} got a nominee for leading role with {p:.1f}!")
        break
if p < 1250.5:
    print(f"Sorry, {a} you need {(1250.5 - p):.1f} more!")