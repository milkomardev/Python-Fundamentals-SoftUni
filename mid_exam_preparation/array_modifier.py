numbers = [int(x) for x in input().split()]
command = input()

while command != 'end':
    command_args = command.split()
    action = command_args[0]
    if action == 'swap':
        first = int(command_args[1])
        second = int(command_args[2])
        numbers[first], numbers[second] = numbers[second], numbers[first]

    elif action == 'multiply':
        first = int(command_args[1])
        second = int(command_args[2])
        numbers[first] = numbers[first] * numbers[second]
    elif action == 'decrease':
        numbers = [x - 1 for x in numbers]

    command = input()

print(*numbers, sep=', ')
