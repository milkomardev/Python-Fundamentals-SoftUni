password = input()
command = input()


while command != "Done":
    command = command.split()
    action = command[0]
    no_substring = False

    if action == "TakeOdd":
        password = password[1::2]

    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index + length:]

    elif action == "Substitute":
        substring = command[1]
        replacement = command[2]
        if substring in password:
            password = password.replace(substring, replacement)
        elif substring not in password:
            no_substring = True
            print('Nothing to replace!')

    if not no_substring:
        print(password)

    command = input()

print(f'Your password is: {password}')
