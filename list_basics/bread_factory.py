energy = 100
coins = 100

line = input().split('|')
flag = True
for event in line:
    event_args = event.split('-')
    name = event_args[0]
    number = int(event_args[1])
    if name == 'rest':
        if energy + number > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            gained_energy = number
            energy += number
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif name == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= number:
            coins -= number
            print(f'You bought {name}.')
        else:
            print(f'Closed! Cannot afford {name}.')
            flag = False
            break

if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
    