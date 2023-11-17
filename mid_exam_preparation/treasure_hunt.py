chest = input().split('|')
command = input()
is_empty = False

while command != 'Yohoho!':
    command_args = command.split()
    action = command_args[0]
    if action == 'Loot':
        for item in range(1, len(command_args)):
            if command_args[item] not in chest:
                chest.insert(0, command_args[item])
    elif action == 'Drop':
        index = int(command_args[1])
        if not 0 <= index < len(chest):
            command = input()
            continue
        else:
            chest.append(chest[index])
            chest.pop(index)
    elif action == 'Steal':
        count = int(command_args[1])
        stolen_list = []
        if count >= len(chest):
            stolen_list.extend(chest)
            is_empty = True
        else:
            for item in range(count):
                stolen_list.insert(0, chest[-1])
                chest.pop(-1)
        print(', '.join(stolen_list))

    command = input()

total_length_sum = sum([len(x) for x in chest])
avg_gain = total_length_sum / len(chest)

if is_empty:
    print('Failed treasure hunt.')
else:
    print(f'Average treasure gain: {avg_gain:.2f} pirate credits.')
