username = input()
password = input()
pass_key = input()

while pass_key != password:
    pass_key = input()
else:
    print(f'Welcome {username}!')


