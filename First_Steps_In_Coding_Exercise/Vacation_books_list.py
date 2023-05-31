total_pages = int(input())
pages_per_hour = int(input())
deadline_days = int(input())

needed_time =(total_pages // pages_per_hour) // deadline_days
print(needed_time)