deposit = float(input())
months = int(input())
annual_interest_rate = float(input())
interest = deposit * (annual_interest_rate/100) / 12
total = deposit + months * interest

print(total)