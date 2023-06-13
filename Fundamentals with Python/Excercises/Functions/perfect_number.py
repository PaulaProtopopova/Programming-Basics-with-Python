# ----------------------------CONDITION OF THE TASK-----------------------------------
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# • "We have a perfect number!" - if the number is perfect.
# • "It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.


def check_whether_is_perfect(some_number):
    divisors_sum = 0
    for current_num in range(some_number - 1, 0, -1):
        if some_number % current_num == 0:
            divisors_sum += current_num
    if divisors_sum == some_number:
        return "We have a perfect number!"
    return 'It\'s not so perfect.'


number = int(input())
print(check_whether_is_perfect(number))
