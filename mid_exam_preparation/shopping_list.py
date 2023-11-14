start_list = input().split('!')
command = input()

while command != 'Go Shopping!':
    command_list = command.split()
    action = command_list[0]
    if action == 'Urgent':
        item = command_list[1]
        if item not in start_list:
            start_list.insert(0, item)
    elif action == 'Unnecessary':
        item = command_list[1]
        if item in start_list:
            item_index = start_list.index(item)
            start_list.pop(item_index)
    elif action == 'Correct':
        old_item = command_list[1]
        new_item = command_list[2]
        if old_item in start_list:
            old_index = start_list.index(old_item)
            start_list[old_index] = new_item
    elif action == 'Rearrange':
        item = command_list[1]
        if item in start_list:
            item_index = start_list.index(item)
            start_list.pop(item_index)
            start_list.append(item)

    command = input()

print(', '.join(start_list))