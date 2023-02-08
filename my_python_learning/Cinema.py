premiere = 12.00
normal = 7.50
discount = 5.00

typproj = str(input())
numnrows = int(input())
numcols = int(input())
revenue = 0

if typproj == "Premiere":
    revenue = premiere * numnrows * numcols
elif typproj == "Normal":
    revenue = normal * numnrows * numcols
elif typproj == "Discount":
    revenue = discount * numnrows * numcols

print(f"{revenue:.2f} USD")
