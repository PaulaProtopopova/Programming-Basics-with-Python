# ----------------------------------CONDITION OF THE TASK---------------------------------
# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().

def rounded_list_of_numbers(string):
    lst = string.split()
    rounded_list = []
    for element in lst:
        rounded_list.append(round(float(element)))
    return rounded_list


string = input()
print(rounded_list_of_numbers(string))










