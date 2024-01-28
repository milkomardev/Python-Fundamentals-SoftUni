activation_key = input()
command = input()


while command != 'Generate':
    command = command.split('>>>')
    action = command[0]
    no_substring = False

    if action == 'Contains':
        substring = command[1]
        no_substring = True
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print(f"Substring not found!")

    elif action == 'Flip':
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = ''
        if case == 'Upper':
            substring = activation_key[start_index:end_index].upper()
        elif case == 'Lower':
            substring = activation_key[start_index:end_index].lower()
        activation_key = activation_key[:start_index] + substring + activation_key[end_index:]

    elif action == 'Slice':
        start_index = int(command[1])
        end_index = int(command[2])
        item_to_delete = activation_key[start_index:end_index]
        activation_key = activation_key.replace(item_to_delete, '')

    if not no_substring:
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")