budget = float(input()) #affects on the destination
season = input() #affects on his budget
destination = 0
place = 0
money_spent = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        money_spent = 0.3 * budget
    else:
        place = 'Hotel'
        money_spent = 0.7 * budget
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        money_spent = 0.4 * budget
    else:
        place = 'Hotel'
        money_spent = 0.8 * budget
elif budget > 1000:
    destination = 'Europe'
    place = 'Hotel'
    money_spent = 0.9 * budget

print(f"Somewhere in {destination}")
print(f"{place} - {money_spent:.2f}")
