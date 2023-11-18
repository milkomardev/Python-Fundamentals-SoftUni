inventory = input().split(', ')
command = input()

while command != 'Craft!':
    command_args = command.split(' - ')
    action = command_args[0]
    item = command_args[1]
    if action == 'Collect':
        if item not in inventory:
            inventory.append(item)
    elif action == 'Drop':
        if item in inventory:
            inventory.remove(item)
    elif action == 'Combine Items':
        old_item, new_item = item.split(':')
        old_index = inventory.index(old_item)
        if old_item in inventory:
            inventory.insert(old_index + 1, new_item)
    elif action == 'Renew':
        if item in inventory:
            inventory.append(item)
            inventory.remove(item)
    command = input()

print(', '.join(inventory))
