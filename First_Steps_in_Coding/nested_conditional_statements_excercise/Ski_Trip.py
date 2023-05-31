days_stay = int(input())
room_type = input()
mark = input()
price_for_night = 0
total_price = 0

total_price = price_for_night * (days_stay - 1)

if room_type == 'room for one person':
    price_for_night = 18
    total_price = price_for_night * (days_stay - 1)


elif room_type == 'apartment':
    price_for_night = 25
    total_price = price_for_night * (days_stay - 1)

    if days_stay < 10:
        total_price = 0.7 * total_price

    elif 10 < days_stay < 15:
        total_price = 0.65 * total_price

    else:
        total_price = 0.5 * total_price


elif room_type == 'president apartment':
    price_for_night = 35
    total_price = price_for_night * (days_stay - 1)
    if days_stay < 10:
        total_price = 0.9 * total_price

    elif 10 < days_stay < 15:
        total_price = 0.85 * total_price

    else:
        total_price = 0.8 * total_price


if mark == 'positive':
    total_price = 1.25 * total_price
    print(f"{total_price:.2f}")
elif mark == 'negative':
    total_price = 0.9 * total_price
    print(f"{total_price:.2f}")

