constant_num = int(input())
summ = 0
while True:
    current_nums = int(input())
    summ += current_nums

    if summ >= constant_num:
        print(summ)
        break

