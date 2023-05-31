# train_ticket = 150
# items = input().split('|')
# budget = float(input())
# profit = 0
# sell_items = []
# is_valid = True
# for item in items:
#     type_of_item, price_of_item = item.split('->')
#     price_of_item = float(price_of_item)
#     if type_of_item == 'Clothes':
#         if price_of_item > 50:
#             is_valid = False
#     elif type_of_item == 'Shoes':
#         if price_of_item > 35:
#             is_valid = False
#     elif type_of_item == 'Accessories':
#         if price_of_item > 20.50:
#             is_valid = False
#     if is_valid:
#         if budget >= price_of_item:
#             budget -= price_of_item
#             sell_price = price_of_item * 1.4
#             profit = sell_price - price_of_item
#             sell_items.append(sell_price)
# for item in sell_items:
#     print(f'{item:.2f}', end=' ')
# print()
# print(f"Profit: {profit:.2f}")
# total_income = budget + sum(sell_items)
# if total_income >= train_ticket:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
#
#
#
# # print(f'{sell_items:.2f}')
# # print(f'{profit:.2f}')
# # if budget >= train_ticket:
# #     print('Hello, France!')
# # else:
# #     print("Not enough money.")
items = input().split("|")
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150
for item in items:
    type, buying_price = item.split("->")
    buying_price = float(buying_price)
    price_is_valid = False
    if type == "Clothes":
        if buying_price <= 50.00:
            price_is_valid = True
    elif type == "Shoes":
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == "Accessories":
        if buying_price <= 20.50:
            price_is_valid = True
    if price_is_valid:
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.40
            profit += sell_price - buying_price
            sell_prices.append(sell_price)
# Option 1
for sell_price in sell_prices:
    print(f"{sell_price:.2f}", end=" ")
print()

# Option 2
# print(" ".join([f"{sell_price:.2f}" for sell_price in sell_prices]))

# Option 3
# sell_prices_as_string = []
# for sell_price in sell_prices:
#     sell_prices_as_string.append(f"{sell_price:.2f}")
# print(" ".join(sell_prices_as_string))

print(f"Profit: {profit:.2f}")
total_income = budget + sum(sell_prices)
if total_income >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")