screening_type = input()
rows = int(input())
columns = int(input())
price = 0

if screening_type == 'Premiere':
    price = 12.00
    full_hall_income = (rows * columns) * price
    print(f'{full_hall_income:.2f} leva')
elif screening_type == 'Normal':
    price = 7.50
    full_hall_income = (rows * columns) * price
    print(f'{full_hall_income:.2f} leva')
elif screening_type == 'Discount':
    price = 5.00
    full_hall_income = (rows * columns) * price
    print(f'{full_hall_income:.2f} leva')
