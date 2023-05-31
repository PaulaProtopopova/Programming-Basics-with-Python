from decimal import Decimal
meters = int(input())

kilometers = meters/1000
kilometers = Decimal(kilometers)
print(f'{kilometers:.2f}')