money_as_string = input().split(', ')
number_of_beggars = int(input())
money_as_values = []

for element in money_as_string:
    money_as_values.append(int(element))
start_index = 0
final_list = []
while start_index < number_of_beggars:
    sum_of_each_beggar = 0
    for current_index in range(start_index, len(money_as_values), number_of_beggars):
        sum_of_each_beggar += money_as_values[current_index]
    final_list.append(sum_of_each_beggar)
    start_index += 1
print(final_list)











