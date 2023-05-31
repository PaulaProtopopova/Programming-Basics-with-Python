str_one = input()
str_two = input()
last_printed_string = str_one
for character_index in range(len(str_one)):
    left_part = str_two[:character_index + 1]
    right_part = str_one[character_index + 1:]
    new_string = left_part + right_part
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string