# ----------------------------CONDITION OF THE TASK--------------------------------
# Write a function that receives two characters and returns a single string with all the characters
# in between them (according to the ASCII code), separated by a single space. Print the result on the console.


def characters_in_range(first_character, second_character):
    all_symbols_between = []
    for character in range(ord(first_character) + 1, ord(second_character)):
        all_symbols_between.append(chr(character))
    return all_symbols_between


first_character = input()
second_character = input()
result = characters_in_range(first_character, second_character)
print(*result)

