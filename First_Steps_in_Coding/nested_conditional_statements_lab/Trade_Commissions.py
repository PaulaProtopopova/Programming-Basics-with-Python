town = input()
s = float(input())
commision = 0

if town == 'Sofia':
    if 0 <= s <= 500:
        commision = 0.05
    elif 500 < s <= 1000:
        commision = 0.07
    elif 1000 < s <= 10000:
        commision = 0.08
    elif s > 10000:
        commision = 0.12
    total_commision = commision * s
    if total_commision <= 0:
        print('error')
    else:
        print(f'{total_commision:.2f}')
elif town == 'Varna':
    if 0 <= s <= 500:
        commision = 0.045
    elif 500 < s <= 1000:
        commision = 0.075
    elif 1000 < s <= 10000:
        commision = 0.1
    elif s > 10000:
        commision = 0.13
    total_commision = commision * s
    if total_commision <= 0:
            print('error')
    else:
            print(f'{total_commision:.2f}')
elif town == 'Plovdiv':
    if 0 <= s <= 500:
        commision = 0.055
    elif 500 < s <= 1000:
        commision = 0.08
    elif 1000 < s <= 10000:
        commision = 0.12
    elif s > 10000:
        commision = 0.145
    total_commision = commision * s
    if total_commision <= 0:
        print('error')
    else:
        print(f'{total_commision:.2f}')
else:
    print('error')

