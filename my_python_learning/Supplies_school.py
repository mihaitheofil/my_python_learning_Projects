pens_price = 5.8
markers_price = 7.2
detergent_price = 1.2
pens_packs = int(input())
markers_packs = int(input())
detergent_packs = int(input())
discount = int(input())
sum = pens_packs * pens_price + markers_packs * markers_price + detergent_packs * detergent_price
rise = round((sum - sum * discount / 100),3)
print(rise)