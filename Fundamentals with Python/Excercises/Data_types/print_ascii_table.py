init_index = int(input())
last_index = int(input())

for index in range(init_index, last_index + 1):
    symbol = chr(index)
    print(symbol, end = ' ')