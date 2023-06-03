# ------------------------------------------CONDITION OF THE TASK-------------------------------------
# You will receive three integer numbers.
# Write functions named:
# • sum_numbers() that returns the sum of the first two integers
# • subtract() that returns the difference between the returned result of the first function and the third
# integer
# Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as
# parameters. Print the result of the subtract() function on the console.


def sum_numbers(a, b):
     return a + b


def subtract(result, c):
    return result - c

def add_and_subtract(first, second, third):
    sum_of_first_and_second_num = sum_numbers(first, second)
    final_res = subtract(sum_of_first_and_second_num, third)
    return final_res


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))



