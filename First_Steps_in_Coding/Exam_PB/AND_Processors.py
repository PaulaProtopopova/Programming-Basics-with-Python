processors_count = int(input())
workers_count = int(input())
working_days_count = int(input())
total_working_hours = 0
ready_processors = 0
money = 0

from math import floor
# Price for 1 processor is 110.10 lv and 1 is done for 3 hours.

total_working_hours = workers_count * working_days_count * 8
ready_processors = (floor(total_working_hours / 3))

if ready_processors < processors_count:
    processors_count = processors_count - ready_processors
    money = processors_count * 110.10
    print(f'Losses: -> {money:.2f} BGN')
elif ready_processors >= processors_count:
    processors_count = ready_processors - processors_count
    money = processors_count * 110.10
    print(f'Profit: -> {money:.2f} BGN')

