sqr_m = float(input())
sum_greening = sqr_m * 7.61
discount = 0.18 * sum_greening
final_price = sum_greening - discount

print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount} lv.')