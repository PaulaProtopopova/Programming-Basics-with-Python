tournaments_count = int(input())
start_points = int(input())
final_points = start_points
average = 0
won_tournaments = 0

for i in range(1, tournaments_count + 1):
    personal_result = input()

    if personal_result == 'W':
        final_points = final_points + 2000
        won_tournaments += 1
    elif personal_result == "F":
        final_points = final_points + 1200
    elif personal_result == 'SF':
        final_points = final_points + 720

print(f'Final points: {final_points}')
average = (final_points - start_points) / tournaments_count
from math import floor
print(f'Average points: {floor(average)}')
won_tournaments = won_tournaments / tournaments_count * 100
print(f'{won_tournaments:.2f}%')
