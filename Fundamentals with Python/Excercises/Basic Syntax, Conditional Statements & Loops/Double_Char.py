

while True:
    string = input()
    if string == 'End':
        break
    elif string == 'SoftUni':
        continue
    else:
        result = ''
        for letter in string:
            result += letter * 2
        print(result)
