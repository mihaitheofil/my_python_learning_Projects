price = 7.61
discount_percentage = 18
area = float(input())
total_price = area * price
discount = total_price * discount_percentage / 100
final_price = total_price - discount
print(f"The final price is: {final_price} USD.")
print(f"The discount is: {discount} USD.")

