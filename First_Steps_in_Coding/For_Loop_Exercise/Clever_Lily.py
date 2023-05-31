age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
money_earned = 0
toy = 0
total_sum = 0
brother_count = 0

for i in range(1, age + 1):
    if i % 2 != 0:
        toy += 1
    else:
        brother_count += 1
        money_earned += 10
        total_sum = total_sum + money_earned

result = total_sum + (toy * toy_price) - brother_count
diff = abs(result - washing_machine_price)

if result >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

