key = input().split()
command = input()

while command != 'find':
    filtered_string = ''
    index = 0
    for symbol in command:
        filtered_string += chr(ord(symbol) - int(key[index]))
        index += 1
        if index == len(key):
            index = 0
    coordinates = ''
    if "<" in filtered_string and '>' in filtered_string:
        if filtered_string.index('<') < filtered_string.index('>'):
            coordinates = filtered_string[filtered_string.index('<') + 1: filtered_string.index('>')]

    type_first_index = filtered_string.find('&')
    type_last_index = filtered_string.rfind('&')

    type_of_treasure = filtered_string[type_first_index + 1: type_last_index]
    print(f"Found {type_of_treasure} at {coordinates}")
    command = input()
