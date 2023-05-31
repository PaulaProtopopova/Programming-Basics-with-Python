exam_hour = int(input())
exam_minute = int(input())
arrived_hour = int(input())
arrived_minute = int(input())

exam_time_all_min = exam_minute + (exam_hour * 60)
arrival_time_all_min = arrived_minute + (arrived_hour * 60)

diff_min = abs(exam_time_all_min - arrival_time_all_min)
if arrival_time_all_min > exam_time_all_min:
    print('Late')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours after the start")
    else:
        print(f"{diff_min} minutes after the start")
elif arrival_time_all_min == exam_time_all_min or diff_min <= 30:
    print("On time")
    if diff_min > 0:
        print(f"{diff_min} minutes before the start")
else:
    print('Early')
    if diff_min >= 60:
        hour = diff_min // 60
        minutes = diff_min % 60
        print(f"{hour}:{minutes:02d} hours before the start")

