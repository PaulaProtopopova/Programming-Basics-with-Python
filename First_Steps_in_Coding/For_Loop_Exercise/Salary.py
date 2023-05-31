tabs_count = int(input())
salary = float(input())
fine = 0

for i in range(1, tabs_count + 1):
    current_tab = input()
    if current_tab == 'Facebook':
        fine = fine + 150
    elif current_tab == 'Instagram':
        fine = fine + 100
    elif current_tab == 'Reddit':
        fine = fine + 50

diff = abs(salary - fine)
if salary <= fine:
    print("You have lost your salary.")
else:
    print(f"{diff:.0f}")

