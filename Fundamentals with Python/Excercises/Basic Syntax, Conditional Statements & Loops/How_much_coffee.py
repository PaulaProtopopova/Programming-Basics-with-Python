coffee_needed = 0

while True:
    command = input()

    if command in ['coding', 'dog', 'cat', 'movie']:
        coffee_needed += 1
    elif command in ['CODING', 'DOG', 'CAT', 'MOVIE']:
        coffee_needed += 2
    elif command == 'END':
        break


if coffee_needed <= 5:
    print(coffee_needed)
else:
    print('You need extra sleep')