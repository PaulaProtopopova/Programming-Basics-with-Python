balance = 0

while True:
    deposit = input()
    if deposit == 'NoMoreMoney':
        break
    deposit = float(deposit)

    if deposit >= 0:
        balance += deposit
        print(f'Increase: {deposit:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {balance:.2f}')