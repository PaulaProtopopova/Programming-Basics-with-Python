max_num = - 9223372036854775807
while True:
    number = input()
    if number != 'Stop':
        number = int(number)
        if number > max_num:
         max_num = number
    else:
        break

print(max_num)


