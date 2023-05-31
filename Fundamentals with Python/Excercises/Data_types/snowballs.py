number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_value = 0
max_quality = 0
for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_snowball_value = (snowball_weight / time_needed) ** quality
    if current_snowball_value > max_value:
        max_value = current_snowball_value
        max_weight = snowball_weight
        max_time = time_needed
        max_quality = quality
print(f'{max_weight} : {max_time} = {max_value:.0f} ({max_quality})')

