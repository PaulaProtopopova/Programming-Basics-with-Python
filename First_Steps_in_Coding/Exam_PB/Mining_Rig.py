video_card_price = int(input())
transition_price = int(input())
consumed_electricity = float(input())
earning_per_day_from_card = float(input())
total_earnings_per_day = 0
money_spent = 0
days_to_return_money = 0

video_card_price = video_card_price * 13
transition_price = transition_price * 13
money_spent = video_card_price + transition_price + 1000
earning_per_day_from_card = earning_per_day_from_card - consumed_electricity
total_earnings_per_day = earning_per_day_from_card * 13

days_to_return_money = money_spent / total_earnings_per_day

from math import ceil

print(money_spent)
print(ceil(days_to_return_money))


