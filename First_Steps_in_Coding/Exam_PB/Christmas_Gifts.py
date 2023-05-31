age = input()
kids = 0
adults = 0
money = 0
money_k = 0

#price for jumper = 15 lv
#price for a toy = 5 lv

while True:
    if age == 'Christmas':
        break
    else:
        age = int(age)

    if age <= 16:
        kids += 1
        money_k = 5 * kids
    else:
        adults += 1
        money = 15 * adults

    age = input()

print(f'Number of adults: {adults}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {money_k}')
print(f'Money for sweaters: {money}')







