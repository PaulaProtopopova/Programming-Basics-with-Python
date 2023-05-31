initial_energy = 100
initial_coins = 100
events = input().split('|')
is_open = True
type_of_event = ''
for event in events:
    event_items = event.split('-')
    type_of_event = event_items[0]
    number = int(event_items[1])
    if type_of_event == 'rest':
        current_energy = initial_energy
        initial_energy += number
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {initial_energy}.')
    elif type_of_event == 'order':
        if initial_energy >= 30:  # order can be completed
            initial_energy -= 30
            initial_coins += number
            print(f'You earned {number} coins.')
        else:
            initial_energy += 50
            print("You had to rest!")
    else:
        if initial_coins >= number:
            initial_coins -= number
            print(f'You bought {type_of_event}.')
        else:
            is_open = False
            break
if is_open:
    print('Day completed!')
    print(f'Coins: {initial_coins}')
    print(f'Energy: {initial_energy}')
else:
    print(f'Closed! Cannot afford {type_of_event}.')






