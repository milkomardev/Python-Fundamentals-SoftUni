def is_valid_index(index, ship):
    return 0 <= index < len(ship)


pirate_ship = [int(x) for x in input().split('>')]
warship = [int(x) for x in input().split('>')]
MAX_HEALTH = int(input())
command = input()
is_sunken = False

while command != 'Retire':
    command_args = command.split()
    if command_args[0] == 'Fire':
        index = int(command_args[1])
        damage = int(command_args[2])
        if is_valid_index(index, warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                is_sunken = True
                break
    elif command_args[0] == 'Defend':
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        damage = int(command_args[3])
        if is_valid_index(start_index, pirate_ship) and is_valid_index(end_index, pirate_ship):
            for section in range(start_index, end_index + 1):
                pirate_ship[section] -= damage
                if pirate_ship[section] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    is_sunken = True
                    break
    elif command_args[0] == 'Repair':
        index = int(command_args[1])
        health = int(command_args[2])
        if is_valid_index(index, pirate_ship):
            pirate_ship[index] = min(MAX_HEALTH, health + pirate_ship[index])
    elif command_args[0] == 'Status':
        need_repair = [x for x in pirate_ship if x < MAX_HEALTH * 0.2]
        print(f'{len(need_repair)} sections need repair.')

    command = input()

if not is_sunken:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')