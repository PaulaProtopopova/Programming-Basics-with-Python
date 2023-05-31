min_num = 9223372036854775807
while True:
    number = input()
    if number != 'Stop':
        number = int(number)
        if number < min_num:
         min_num = number
    else:
        break
print(min_num)

