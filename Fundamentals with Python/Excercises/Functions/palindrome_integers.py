# ------------------CONDITION OF THE TASK----------------------
# A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
# Write a function that receives a list of positive integers, separated by comma and space ", ".
# The function should check if each integer is a palindrome - True or False. Print the result.

def check_palindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False

numbers = input().split(', ')
for number in numbers:
    print(check_palindrome(number))







