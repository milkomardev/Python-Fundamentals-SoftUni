text = input().split()

while True:
    command = input()

    if command == '3:1':
        print(' '.join(text))
        break

    command = command.split()

    if command[0] == 'merge':
        start_index = int(command[1])
        end_index = int(command[2])
        new_word = ''
        counter = 0
        if start_index >= len(text):
            start_index = 0
        if end_index > len(text):
            end_index = len(text)-1

        for el in range(max(start_index, 0), min(end_index + 1, len(text))):
            new_word += text[el]
            counter += 1

        [text.pop(start_index) for word in range(counter)]

        text.insert(start_index, new_word)

    elif command[0] == 'divide':
        index = int(command[1])
        partitions = int(command[2])

        element = text[index]
        elements_parts = []
        chr_per_part = len(element) // partitions

        current_partition = ''
        for el in range((partitions - 1) * chr_per_part):
            current_partition += element[el]
            if len(current_partition) == chr_per_part:
                elements_parts.append(current_partition)
                current_partition = ''

        for el in range((partitions - 1) * chr_per_part, len(element)):
            current_partition += element[el]
        elements_parts.append(current_partition)

        text.pop(index)

        elements_parts.reverse()

        for part in elements_parts:
            text.insert(index, part)
