actor_name = input()
academy_points = float(input())
jury_count = int(input())
score_total = academy_points

for i in range(1, jury_count + 1):
    jury_name = input()
    jury_points = float(input())

    current_points = (len(jury_name) * jury_points)/2
    score_total = current_points + score_total

    if score_total >= 1250.5:
        break

if score_total >= 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {score_total:.1f}!')
else:
    diff = 1250.5 - score_total
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")