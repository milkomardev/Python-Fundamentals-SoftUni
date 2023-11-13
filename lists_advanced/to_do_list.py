command = input()
list_of_commands_asc = [''] * 10

while command != 'End':
    index, note = command.split('-')
    index = int(index)
    list_of_commands_asc[index-1] += note
    command = input()

print([note for note in list_of_commands_asc if note != ''])
