def is_valid_index(index, sequence):
    return 0 <= index < len(sequence)


elements = input().split()
command = input()
moves = 0

while command != 'end':
    moves += 1
    indexes = [int(x) for x in command.split()]
    first = indexes[0]
    second = indexes[1]
    if not is_valid_index(first, elements) or not is_valid_index(second, elements) or first == second:
        for _ in range(2):
            elements.insert(len(elements)//2, f'-{moves}a')
        print('Invalid input! Adding additional elements to the board')
    else:
        if elements[first] == elements[second]:
            print(f'Congrats! You have found matching elements - {elements[first]}!')
            char = elements[second]
            elements.pop(first)
            elements.remove(char)
            if not elements:
                print(f'You have won in {moves} turns!')
                exit(0)
        else:
            print('Try again!')

    command = input()

else:
    print(f"Sorry you lose :(")
    print(' '.join(elements))
