list_of_nums = input().split()
numeric_list = []
for element in list_of_nums:
    number = int(element)
    numeric_list.append(number)
remover = int(input())
for _ in range(remover):
    numeric_list.remove(min(numeric_list))
print(*numeric_list, sep=", ")


