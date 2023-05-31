n = int(input())
sum_of_digits = 0

for num in range(1, n + 1):
    str_num = str(num)
    for string in str_num:
        digit = int(string)
        sum_of_digits += digit
    if sum_of_digits in [5,7,11]:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
    sum_of_digits = 0