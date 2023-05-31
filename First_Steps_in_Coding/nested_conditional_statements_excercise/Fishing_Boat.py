group_budget = int(input())
season = input()
count_fishers = int(input())
price = 0

if season == 'Spring':
    price = 3000
elif season in ['Summer', 'Autumn']:
    price = 4200
elif season == 'Winter':
    price = 2600

if count_fishers <= 6:
    price = 0.9 * price
elif 6 < count_fishers <= 11:
    price = 0.85 * price
elif count_fishers >= 12:
    price = 0.75 * price

if count_fishers % 2 == 0 and season in ['Spring', 'Summer', 'Winter']:
    price = 0.95 * price

diff = abs(group_budget - price)

if group_budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")

