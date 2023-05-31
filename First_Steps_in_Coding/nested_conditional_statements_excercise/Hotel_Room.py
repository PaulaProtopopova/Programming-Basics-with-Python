month = input()
stay = int(input())
price_studio = 0
price_flat = 0

if month in ['May', 'October']:
    price_studio = 50.00 * stay
    price_flat = 65.00 * stay
    if 7 < stay <= 14:
        price_studio = 0.95 * price_studio
    elif stay > 14:
        price_studio = 0.7 * price_studio
        price_flat = 0.9 * price_flat

elif month in ['June', 'September']:
    price_studio = 75.20 * stay
    price_flat = 68.70 * stay
    if stay > 14:
        price_studio = 0.8 * price_studio
        price_flat = 0.9 * price_flat

elif month in ['July', 'August']:
    price_studio = 76.00 * stay
    price_flat = 77.00 * stay
    if stay > 14:
        price_flat = 0.9 * price_flat

print(f"Apartment: {price_flat:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")