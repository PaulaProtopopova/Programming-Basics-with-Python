groups_count = int(input())
musala_sum = 0
monblan_sum = 0
kilimandjaro_sum = 0
k_two_sum = 0
everest = 0
total_people = 0
# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест

for i in range(1, groups_count + 1):
    climbers_count = int(input())

    if climbers_count <= 5:
        musala_sum = musala_sum + climbers_count
    elif climbers_count <= 12:
        monblan_sum = monblan_sum + climbers_count
    elif climbers_count <= 25:
        kilimandjaro_sum = kilimandjaro_sum + climbers_count
    elif climbers_count <= 40:
        k_two_sum = k_two_sum + climbers_count
    elif climbers_count >= 41:
        everest = everest + climbers_count

total_people = musala_sum + monblan_sum + kilimandjaro_sum + k_two_sum + everest

musala_sum = musala_sum / total_people * 100
monblan_sum = monblan_sum / total_people * 100
kilimandjaro_sum = kilimandjaro_sum / total_people * 100
k_two_sum = k_two_sum / total_people * 100
everest = everest / total_people * 100

print(f'{musala_sum:.2f}%')
print(f'{monblan_sum:.2f}%')
print(f'{kilimandjaro_sum:.2f}%')
print(f'{k_two_sum:.2f}%')
print(f'{everest:.2f}%')