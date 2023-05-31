while True:
    name = input()

    if len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6 and name not in ['Welcome!', 'Voldemort']:
        print(f'{name} goes to Hufflepuff.')
    elif name == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
