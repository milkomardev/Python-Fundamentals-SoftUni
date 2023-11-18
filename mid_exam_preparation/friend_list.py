def is_valid_index(index, seq):
    return 0 <= index < len(seq)


friends = input().split(', ')
command = input()
blacklisted_names = 0
lost_names = 0

while command != 'Report':
    command_args = command.split()
    action = command_args[0]
    if action == 'Blacklist':
        name = command_args[1]
        if name in friends:
            index_name = friends.index(name)
            print(f'{name} was blacklisted.')
            friends[index_name] = 'Blacklisted'
            blacklisted_names += 1
        else:
            print(f'{name} was not found.')

    elif action == 'Error':
        index = int(command_args[1])
        if is_valid_index(index, friends) and (friends[index] != 'Lost' and friends[index] != 'Blacklisted'):
            print(f'{friends[index]} was lost due to an error.')
            friends[index] = 'Lost'
            lost_names += 1

    elif action == 'Change':
        index = int(command_args[1])
        new_name = command_args[2]
        if is_valid_index(index, friends):
            print(f'{friends[index]} changed his username to {new_name}.')
            friends[index] = new_name

    command = input()

print(f'Blacklisted names: {blacklisted_names}')
print(f'Lost names: {lost_names}')
print(' '.join(friends))
