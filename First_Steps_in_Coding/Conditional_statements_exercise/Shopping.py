petars_budget = float(input())
n_count = int(input())
m_count = int(input())
p_count = int(input())

n_price = n_count * 250
m_price = (0.35 * n_price) * m_count
p_price = (0.1 * n_price) * p_count
price_total = n_price + m_price + p_price

if n_count > m_count:
    price_total = price_total - (0.15 * price_total)

diff = abs(petars_budget - price_total)
if price_total <= petars_budget:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')
