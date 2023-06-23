# # --------------------------------CONDITION OF THE TASK-----------------------------------
# On the first line, you will receive words separated by a single space.
# On the second line, you will receive a palindrome.
# First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format:
# "Found palindrome {number} times".

def is_palindrome(word):
    if word == word[::-1]:
        return word

words = input().split()
searched_palindrome = input()

palindrome_list = [word for word in words if is_palindrome(word)]
palindrome_counter = palindrome_list.count(searched_palindrome)

print(palindrome_list)
print(f'Found palindrome {palindrome_counter} times')