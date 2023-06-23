#-----------------------------CONDITION OF THE TASK--------------
# Write a program that reads a single string with numbers
# separated by comma and space ", ".
# Print the indices of all even numbers.


def even_numbers():
    indeces = list(numbers.index(number) for number in numbers if number % 2 == 0)
    return indeces


numbers = list(map(int, input().split(', ')))

print(even_numbers())
