name = input()
grades_total = 0
years_counter = 0
failed_years = 0

while True:
    mark = float(input())
    grades_total += 1
    if mark < 4:
        failed_years += 1
        if failed_years == 2:
                print(f'"{name} has been excluded at {grades_total} grade')


