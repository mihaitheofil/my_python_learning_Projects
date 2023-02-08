chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15
delivery_price = 2.50

chicken_menues = int(input())
fish_menues = int(input())
vegetarian_menues = int(input())

# dessert = 20% of total bill
menues = chicken_menues * chicken_menu + fish_menues * fish_menu + vegetarian_menues * vegetarian_menu
dessert = 0.2 * menues
order_price = menues + dessert + delivery_price

print(order_price)