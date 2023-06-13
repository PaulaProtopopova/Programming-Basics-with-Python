# --------------------------CONDITION OF THE TASK-----------------------------
# Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min
# and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
# The output should be as follows:
# • On the first line: "The minimum number is {minimum number}"
# • On the second line: "The maximum number is {maximum number}"
# • On the third line: "The sum number is: {sum of all numbers}"

numbers_as_str = input().split()
numbers_as_digits = list(map(int, numbers_as_str))
max_num = max(numbers_as_digits)
min_num = min(numbers_as_digits)
total_sum = sum(numbers_as_digits)

print(f'The minimum number is {min_num}')
print(f'The maximum number is {max_num}')
print(f'The sum number is: {total_sum}')