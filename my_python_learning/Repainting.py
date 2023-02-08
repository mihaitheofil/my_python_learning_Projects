nylon_price = 1.50
paint_price = 14.50
detergent_price = 5.00
extra_paint = 1.1
extra_nylon = 2
bags_price = 0.40
nylon_meters = int(input())
nylon_total = round((nylon_price * (nylon_meters + extra_nylon)),3)
# print(f'Nylon: {nylon_total}')

paint_liters = int(input())
paint_total = round((paint_price * paint_liters * extra_paint),3)
# print(f'Paint: {paint_total}')

detergent_liters = int(input())
detergent_total = round((detergent_price * detergent_liters),3)
# print(f'Detergent: {detergent_total}')

work_hours = int(input())


sum_materials = nylon_total + paint_total + detergent_total + bags_price
# print(f'Sum materials: {sum_materials}')

work_cost = sum_materials * 0.3 * work_hours
# print(f'Workers: {work_cost}')

total_sum = sum_materials + work_cost
print(total_sum)