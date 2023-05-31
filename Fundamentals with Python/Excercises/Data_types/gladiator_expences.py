lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
broken_helmets_count = lost_fights_count // 2
broken_swords_count = lost_fights_count // 3
broken_shields_count = lost_fights_count // (2*3)
broken_armor_count = broken_shields_count // 2
expences = shield_price * broken_shields_count + helmet_price * broken_helmets_count + sword_price * broken_swords_count + armor_price * broken_armor_count
print(f'Gladiator expenses: {expences:.2f} aureus')

