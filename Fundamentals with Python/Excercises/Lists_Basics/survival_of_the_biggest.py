#CONDITION OF TASK:
# Write a program that receives a list of integer numbers (separated by a single space)
# and a number n. The number n represents the count of numbers to remove from the list.
# should remove the smallest ones, and then, you should print all the numbers that are left in the list, separated by a comma and a space ", ".


#FIRST OPTION
# list_of_nums = input().split()
# numeric_list = []
# for element in list_of_nums:
#     number = int(element)
#     numeric_list.append(number)
# remover = int(input())
# for _ in range(remover):
#     numeric_list.remove(min(numeric_list))
# print(*numeric_list, sep=", ")

#OPTIMIZED
numbers = list(map(int, input().split()))
remover = int(input())
for _ in range(remover):
    numbers.remove(min(numbers))
print(*numbers, sep=", ")
