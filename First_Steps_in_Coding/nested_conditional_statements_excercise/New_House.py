type_flowers = input()
count = int(input())
budget = int(input())

sum = 0
if type_flowers == 'Roses':
    sum = count * 5.00
    if count > 80:
        #10% discount
        sum = 0.9 * sum
elif type_flowers == 'Dahlias':
    sum = count * 3.80
    if count > 90:
        #15% discount
        sum = 0.85 * sum

elif type_flowers == 'Tulips':
    sum = count * 2.80
    if count > 80:
        #15% discount
        sum = 0.85 * sum

elif type_flowers == 'Narcissus':
    sum = count * 3.00
    if count < 120:
        #oskupqva se s 15%
        sum = 1.15 * sum

elif type_flowers == 'Gladiolus':
    sum = count * 2.50
    if count < 80:
        #oskupqva se s 20%
        sum = 1.2 * sum

diff = abs(budget - sum)

if budget >= sum:
    print(f"Hey, you have a great garden with {count} {type_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")

