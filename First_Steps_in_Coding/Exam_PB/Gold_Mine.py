
locations = int(input())


for i in range(locations):
    planned_mined_gold = float(input())
    days_count = int(input())
    total_gold_for_location = 0
    average_gold_per_location = 0
    for _ in range(days_count):
        mined_gold_per_day = float(input())
        total_gold_for_location += mined_gold_per_day
    average_gold_per_location = (total_gold_for_location / days_count)
    if average_gold_per_location >= planned_mined_gold:
        print(f"Good job! Average gold per day: {average_gold_per_location:.2f}.")
    else:
        print(f"You need {(planned_mined_gold - average_gold_per_location):.2f} gold.")
