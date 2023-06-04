# --------------------------------CONDITION OF THE TASK--------------------------------
# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().



# def even_number(number):
#     if number % 2 == 0:
#         return number

numbers_as_string = list(input().split())
numbers_as_digits = []

for element in numbers_as_string:
        numbers_as_digits.append(int(element))

#OPTION WITH LAMBDA:

is_even = lambda x: x % 2 == 0


result = list(filter(is_even, numbers_as_digits))
print(result)
