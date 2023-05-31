n_one = int(input())
n_two = int(input())
operator = (input())
result = 0
e_o = 0

if operator == '+':
    result = n_one + n_two
    if result % 2 == 0:
        print(f"{n_one} + {n_two} = {result} - even")
    else:
        print(f"{n_one} + {n_two} = {result} - odd")

elif operator == '-':
    result = n_one - n_two
    if result % 2 == 0:
        print(f"{n_one} - {n_two} = {result} - even")
    else:
        print(f"{n_one} - {n_two} = {result} - odd")
elif operator == '*':
    result = n_one * n_two
    if result % 2 == 0:
        print(f"{n_one} * {n_two} = {result} - even")
    else:
        print(f"{n_one} * {n_two} = {result} - odd")
elif operator == '/' and n_two != 0:
    result = n_one / n_two
    print(f"{n_one} / {n_two} = {result:.2f}")
elif operator == "%" and n_two != 0:
    result = n_one % n_two
    print(f"{n_one} % {n_two} = {result}")

if n_two == 0:
    print(f"Cannot divide {n_one} by zero")



