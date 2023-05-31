basketball_fee = int(input())

sneakers = basketball_fee - (0.4 * basketball_fee)
equipment = sneakers - (0.2 * sneakers)
ball = equipment / 4
accessories = ball / 5

total = sneakers + basketball_fee + equipment + ball + accessories
print(total)