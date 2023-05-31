from sys import maxsize

divisor = int(input())
boundary = int(input())

max_num = -maxsize
for number in range(boundary + 1):
    if number % divisor == 0:
        max_num = number

print(max_num)