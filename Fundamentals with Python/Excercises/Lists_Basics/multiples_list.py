factor = int(input())
count = int(input())
start_point = 1
list = []

for number in range(count):
    multiplied_number = start_point * factor
    list.append(multiplied_number)
    start_point += 1
print(list)
