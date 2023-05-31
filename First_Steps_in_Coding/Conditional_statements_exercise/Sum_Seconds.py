time_first = int(input())
time_second = int(input())
time_third = int(input())

sum_all_seconds = time_first + time_second + time_third
minutes = sum_all_seconds // 60
total_seconds = sum_all_seconds % 60

if total_seconds < 10:
    print(f'{minutes}:0{total_seconds}')

else:
    print(f'{minutes}:{total_seconds}')
