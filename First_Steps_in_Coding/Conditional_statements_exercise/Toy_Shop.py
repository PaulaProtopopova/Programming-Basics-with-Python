price_vacation = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())



total_sum = (puzzles_count * 2.60) + (dolls_count * 3.00) + (teddy_bears_count * 4.10) + (minions_count * 8.20) + (trucks_count * 2)

total_count_toys = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count

if total_count_toys >= 50:
    total_sum = total_sum - (total_sum * 0.25)

total_sum = total_sum - (0.1 * total_sum)

diff = abs(price_vacation - total_sum)
if total_sum >= price_vacation:
    print(f"Yes! {diff:.2f} lv left.")

else:
    print(f"Not enough money! {diff:.2f} lv needed.")