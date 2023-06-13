# --------------------------------------CONDITION OF THE TASK----------------------------------------
# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point

def factorial(number):
    for current_num in range(1, number):
        number *= current_num
    return number


num_one = int(input())
num_two = int(input())
first_factorial = factorial(num_one)
second_factorial = factorial(num_two)
division = first_factorial / second_factorial

print(f'{division:.2f}')