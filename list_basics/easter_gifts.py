gifts = input().split()

while True:
    line = input()
    if line == 'No Money':
        break

    command_parts = line.split()
    command = command_parts[0]
    item = command_parts[1]

    if command == 'OutOfStock':
        for idx in range(len(gifts)):
            if gifts[idx] == item:
                gifts[idx] = 'None'
    elif command == 'Required':
        index = int(command_parts[2])
        if 0 <= index <= len(gifts):
            gifts[index] = item
    else:
        gifts[-1] = item

for gift in gifts:
    if gift == 'None':
        continue
    else:
        print(gift, end=' ')