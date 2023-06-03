# ----------------------------------CONDITION OF THE TASK---------------------------------
# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

list = input().split()
rounded_lst = []


for element in list:
    number = float(element)
    rounded_lst.append(round(number))

print(rounded_lst)




