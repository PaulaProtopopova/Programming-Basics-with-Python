n = int(input())
filtered_lst = []
initial_list = []
for _ in range(n):
    number = int(input())
    initial_list.append(number)
command = input()

if command == 'even':
    for number in initial_list:
        if number % 2 == 0:
            filtered_lst.append(number)
elif command == 'odd':
    for number in initial_list:
        if number % 2 != 0:
            filtered_lst.append(number)
elif command == 'negative':
    for number in initial_list:
        if number < 0:
            filtered_lst.append(number)
elif command == 'positive':
    for number in initial_list:
        if number > 0:
            filtered_lst.append(number)

print(filtered_lst)

