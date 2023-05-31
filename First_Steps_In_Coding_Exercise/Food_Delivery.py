chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

price_for_chiken_menu = chicken_menu * 10.35
price_for_fish_menu = fish_menu * 12.40
price_for_veggie_menu = veggie_menu * 8.15

total_price = price_for_fish_menu + price_for_veggie_menu + price_for_chiken_menu
price_dessert = 0.2 * total_price

#Price for delivery is 2.50.

order_total = total_price + price_dessert + 2.50
print(f"{order_total:.2f}")