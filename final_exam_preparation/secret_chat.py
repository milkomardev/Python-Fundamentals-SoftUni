text = input()
command = input()

while command != "Reveal":
    args = command.split(':|:')
    action = args[0]
    if action == 'InsertSpace':
        index = int(args[1])
        text = text[:index] + ' ' + text[index:]

    elif action == 'Reverse':
        substring = args[1]
        if substring in text:
            text = text.replace(substring, '', 1)
            substring = substring[::-1]
            text += substring
        else:
            print('error')
            command = input()
            continue

    elif action == 'ChangeAll':
        substring = args[1]
        replacement = args[2]
        text = text.replace(substring, replacement)
    print(text)
    command = input()

print(f"You have a new text message: {text}")
