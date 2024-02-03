def is_valid_index(index, seq):
    return 0 <= index < len(seq)


stops = input()

command = input()
while command != 'Travel':
    command_args = command.split(':')
    action = command_args[0]
    if action == 'Add Stop':
        index = int(command_args[1])
        new_stop = command_args[2]
        if is_valid_index(index, stops):
            stops = stops[:index] + new_stop + stops[index:]
    elif action == 'Remove Stop':
        start_index = int(command_args[1])
        stop_index = int(command_args[2])
        if is_valid_index(start_index, stops) and is_valid_index(stop_index, stops):
            stops = stops[:start_index] + stops[stop_index + 1:]
    elif action == 'Switch':
        old_stop = command_args[1]
        new_stop = command_args[2]
        stops = stops.replace(old_stop, new_stop)
    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
