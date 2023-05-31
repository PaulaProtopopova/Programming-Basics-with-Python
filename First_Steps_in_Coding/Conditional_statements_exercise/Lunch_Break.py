from math import ceil

name_of_series = input()
episode_lenght = int(input())
lunch_break_lenght = int(input())

time_for_lunch = 1/8 * lunch_break_lenght
time_for_rest = 1/4 * lunch_break_lenght
time_left = lunch_break_lenght - time_for_lunch - time_for_rest

diff = abs(time_left - episode_lenght)
rounded_diff = ceil(diff)

if time_left >= episode_lenght:
    print(f'You have enough time to watch {name_of_series} and left with {rounded_diff} minutes free time.')

else:
    print(f"You don't have enough time to watch {name_of_series}, you need {rounded_diff} more minutes.")