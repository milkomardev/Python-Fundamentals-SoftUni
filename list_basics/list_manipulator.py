import sys
numbers = [int(x) for x in input().split()]
line = input()

while line != 'end':
    even_count = 0
    odd_count = 0
    line_list = line.split()
    command = line_list[0]
    if command == 'exchange':
        index = int(line_list[1])
        if index < 0 or index >= len(numbers):
            print('Invalid index')
        else:
            numbers = numbers[index + 1:] + numbers[: index + 1]

    elif command == 'max':
        index = line_list[1]
        max_even = -sys.maxsize
        max_even_index = 0
        max_odd = -sys.maxsize
        max_odd_index = 0
        for even_odd in range(len(numbers)):
            if numbers[even_odd] % 2 == 0 and numbers[even_odd] >= max_even:
                max_even = numbers[even_odd]
                max_even_index = even_odd
                even_count += 1
            elif numbers[even_odd] % 2 != 0 and numbers[even_odd] >= max_odd:
                max_odd = numbers[even_odd]
                max_odd_index = even_odd
                odd_count += 1
        if index == 'even':
            if even_count == 0:
                print('No matches')
                line = input()
                continue
            print(max_even_index)
        elif index == 'odd':
            if odd_count == 0:
                print('No matches')
                line = input()
                continue
            print(max_odd_index)
    elif command == 'min':
        index = line_list[1]
        min_even = sys.maxsize
        min_even_index = 0
        min_odd = sys.maxsize
        min_odd_index = 0
        for even_odd in range(len(numbers)):
            if numbers[even_odd] % 2 == 0 and numbers[even_odd] <= min_even:
                min_even = numbers[even_odd]
                min_even_index = even_odd
                even_count += 1
            elif numbers[even_odd] % 2 != 0 and numbers[even_odd] <= min_odd:
                min_odd = numbers[even_odd]
                min_odd_index = even_odd
                odd_count += 1
        if index == 'even':
            if even_count == 0:
                print('No matches')
                line = input()
                continue
            print(min_even_index)
        elif index == 'odd':
            if odd_count == 0:
                print('No matches')
                line = input()
                continue
            print(min_odd_index)
    elif command == 'first':
        count = int(line_list[1])
        index = line_list[2]
        list_even = []
        list_odd = []
        if count > len(numbers):
            print('Invalid count')
            line = input()
            continue
        for even_odd in range(len(numbers)):
            if numbers[even_odd] % 2 == 0:
                list_even.append(numbers[even_odd])
                if len(list_even) == count:
                    break
            elif numbers[even_odd] % 2 != 0:
                list_odd.append(numbers[even_odd])
                if len(list_odd) == count:
                    break
        if index == 'even':
            print(list_even)
        elif index == 'odd':
            print(list_odd)
    elif command == 'last':
        count = int(line_list[1])
        index = line_list[2]
        list_even = []
        list_odd = []
        if count > len(numbers):
            print('Invalid count')
            line = input()
            continue
        for even_odd in range(len(numbers) - 1, -1, -1):
            if numbers[even_odd] % 2 == 0:
                list_even.append(numbers[even_odd])
                if len(list_even) == count:
                    break
            elif numbers[even_odd] % 2 != 0:
                list_odd.append(numbers[even_odd])
                if len(list_odd) == count:
                    break
        if index == 'even':
            print(list_even)
        elif index == 'odd':
            print(list_odd)
    line = input()
print(numbers)
