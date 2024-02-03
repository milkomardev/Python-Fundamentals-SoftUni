message = input()
line = input()
while line != 'Decode':
    line_args = line.split('|')
    command = line_args[0]
    if command == 'Move':
        number = int(line_args[1])
        message = message[number:] + message[:number]
    elif command == 'Insert':
        index = int(line_args[1])
        value = line_args[2]
        message = message[:index] + value + message[index:]
    elif command == 'ChangeAll':
        substring = line_args[1]
        replacement = line_args[2]
        message = message.replace(substring, replacement)
    line = input()

print(f'The decrypted message is: {message}')