def is_valid_index(index, seq):
    return 0 <= index < len(seq)


line = input()
command = input()

while command != 'Finish':
    command = command.split()
    action = command[0]
    if action == 'Replace':
        old_char = command[1]
        new_char = command[2]
        line = line.replace(old_char, new_char)
        print(line)

    elif action == 'Cut':
        start_index = int(command[1])
        end_index = int(command[2])
        if is_valid_index(start_index, line) and is_valid_index(end_index, line):
            line = line[:start_index] + line[end_index+1:]
            print(line)
        else:
            print("Invalid indices!")

    elif action == 'Make':
        case = command[1]
        if case == 'Upper':
            line = line.upper()
        elif case == 'Lower':
            line = line.lower()
        print(line)

    elif action == 'Check':
        string_to_check = command[1]
        if string_to_check in line:
            print(f"Message contains {string_to_check}")
        else:
            print(f"Message doesn't contain {string_to_check}")

    elif action == 'Sum':
        start_index = int(command[1])
        end_index = int(command[2])
        if is_valid_index(start_index, line) and is_valid_index(end_index, line):
            substring = line[start_index:end_index+1]
            chars_in_ascii = [int(ord(char)) for char in substring]
            print(sum(chars_in_ascii))
        else:
            print("Invalid indices!")

    command = input()
