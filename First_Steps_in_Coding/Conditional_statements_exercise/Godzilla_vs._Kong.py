budget = float(input())
statists_count = int(input())
price_clothing_one = float(input())

decor_price = 0.1 * budget
all_clothes_sum = statists_count * price_clothing_one

if statists_count > 150:
    all_clothes_sum = all_clothes_sum * 0.9

total_budget = decor_price + all_clothes_sum
diff = abs(budget - total_budget)

if budget >= total_budget:
    print("Action!")
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")