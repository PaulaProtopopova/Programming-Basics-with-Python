#---------CONDITION OF THE TASK--------------------------
# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print a sorted
# list of numbers in ascending order. Use sorted().


numbers_as_string = list(input().split())
numbers_as_digits = list(int(x) for x in numbers_as_string if type(x) == str)
print(sorted(numbers_as_digits))