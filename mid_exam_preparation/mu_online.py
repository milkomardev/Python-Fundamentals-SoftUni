health = 100
bitcoins = 0
MAX_HEALTH = 100
rooms = input().split('|')
counter = 0
is_dead = False
for room in rooms:
    counter += 1
    room_args = room.split()
    command = room_args[0]
    number = int(room_args[1])
    if command == 'potion':
        if health + number <= MAX_HEALTH:
            print(f'You healed for {number} hp.')
        else:
            print(f'You healed for {MAX_HEALTH - health} hp.')
        health = min(MAX_HEALTH, health + number)
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {counter}')
            is_dead = True
            break

if not is_dead:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')