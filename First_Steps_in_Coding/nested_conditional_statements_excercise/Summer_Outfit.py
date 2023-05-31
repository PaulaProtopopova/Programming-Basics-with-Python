degrees = int(input())
around_time = input()
outfit = 0
shoes = 0

if 10 <= degrees <= 18:
    if around_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif around_time in ['Afternoon', 'Evening']:
        outfit = 'Shirt'
        shoes = 'Moccasins'

elif 18 < degrees <= 24:
    if around_time in ['Morning', 'Evening']:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif around_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif degrees >= 25:
    if around_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif around_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif around_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")