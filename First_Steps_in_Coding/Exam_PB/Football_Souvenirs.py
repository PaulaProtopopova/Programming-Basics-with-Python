team = input()
souvenirs_type = input()
souvenirs_bought = int(input())
money_spent = 0


if team == 'Argentina':
    if souvenirs_type == 'flags':
        money_spent = 3.25 * souvenirs_bought
    elif souvenirs_type == 'caps':
        money_spent = 7.20 * souvenirs_bought
    elif souvenirs_type == 'posters':
        money_spent = 5.10 * souvenirs_bought
    elif souvenirs_type == 'stickers':
        money_spent = 1.25 * souvenirs_bought
    else:
        print("Invalid stock!")
elif team == 'Brazil':
    if souvenirs_type == 'flags':
        money_spent = 4.20 * souvenirs_bought
    elif souvenirs_type == 'caps':
        money_spent = 8.50 * souvenirs_bought
    elif souvenirs_type == 'posters':
        money_spent = 5.35 * souvenirs_bought
    elif souvenirs_type == 'stickers':
        money_spent = 1.20 * souvenirs_bought
    else:
        print("Invalid stock!")
elif team == 'Croatia':
    if souvenirs_type == 'flags':
        money_spent = 2.75 * souvenirs_bought
    elif souvenirs_type == 'caps':
        money_spent = 6.90 * souvenirs_bought
    elif souvenirs_type == 'posters':
        money_spent = 4.95 * souvenirs_bought
    elif souvenirs_type == 'stickers':
        money_spent = 1.10 * souvenirs_bought
    else:
        print("Invalid stock!")
elif team == 'Denmark':
    if souvenirs_type == 'flags':
        money_spent = 3.10 * souvenirs_bought
    elif souvenirs_type == 'caps':
        money_spent = 6.50 * souvenirs_bought
    elif souvenirs_type == 'posters':
        money_spent = 4.80 * souvenirs_bought
    elif souvenirs_type == 'stickers':
        money_spent = 0.90 * souvenirs_bought
    else:
        print("Invalid stock!")
else:
    print("Invalid country!")

if team in ["Argentina", "Brazil", "Croatia", "Denmark"] and souvenirs_type in ["flags", "caps", "posters", "stickers"]:
    print(f"Pepi bought {souvenirs_bought} {souvenirs_type} of {team} for {money_spent:.2f} lv.")




