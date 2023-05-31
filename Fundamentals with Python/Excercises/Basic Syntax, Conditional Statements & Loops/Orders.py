orders_num = int(input())
total_price = 0

for order in range(orders_num):
    price = float(input())
    days = int(input())
    capsules = int(input())

    if price >= 0.01 and price <= 100 and days >= 1 and days <= 31 and capsules >= 1 and capsules <= 2000:
        price = price * capsules * days
        print(f'The price for the coffee is: ${price:.2f}')
        total_price += price

print(f'Total: ${total_price:.2f}')


