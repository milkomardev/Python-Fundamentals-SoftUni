def is_valid_index(index, seq):
    return 0 <= index < len(seq)


targets = [int(x) for x in input().split()]
command = input()

while command != 'End':
    command_args = command.split()
    action = command_args[0]
    index = int(command_args[1])
    number = int(command_args[2])
    if action == 'Shoot':
        if is_valid_index(index, targets):
            targets[index] -= number
            if targets[index] <= 0:
                targets.pop(index)

    elif action == 'Add':
        if not is_valid_index(index, targets):
            print('Invalid placement!')
        else:
            targets.insert(index, number)

    elif action == 'Strike':
        if not is_valid_index(index - number, targets) or not is_valid_index(index + number, targets) \
                or not is_valid_index(index, targets):
            print('Strike missed!')
            command = input()
            continue
        else:
            for _ in range(2*number + 1):
                targets.pop(index - number)

    command = input()

print(*targets, sep='|')
