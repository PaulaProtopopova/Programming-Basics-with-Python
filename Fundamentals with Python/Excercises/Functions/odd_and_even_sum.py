# ------------------------------------CONDITION OF THE TASK----------------------
# You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a
# given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.

# def odd_and_even_sum(nums_string):
#     even_digits = [int(x) for x in nums_string if int(x) % 2 == 0]
#     odd_digits = [int(y) for y in nums_string if int(y) % 2 != 0]
#     sum_of_evens = sum(even_digits)
#     sum_of_odds = sum(odd_digits)
#     return f'Odd sum = {sum_of_odds}, Even sum = {sum_of_evens}'
#
# print(odd_and_even_sum(input()))

#--------OPTION 2 WITH LAMBDA FUNCTION--------------

nums_input = [int(i) for i in input()]
even_digits = list(filter(lambda x: x % 2 == 0, nums_input))
odd_digits = list(filter(lambda y: y % 2 != 0, nums_input))
sum_of_evens = sum(even_digits)
sum_of_odds = sum(odd_digits)
print(f'Odd sum = {sum_of_odds}, Even sum = {sum_of_evens}')












