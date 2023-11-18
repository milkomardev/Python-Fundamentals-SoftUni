def is_valid_index(index, seq):
    return 0 <= index < len(seq)


books = input().split('&')
command = input()

while command != 'Done':
    command_args = command.split(' | ')
    action = command_args[0]
    if action == 'Add Book':
        name = command_args[1]
        if name not in books:
            books.insert(0, name)

    elif action == 'Take Book':
        name = command_args[1]
        if name in books:
            books.remove(name)

    elif action == 'Swap Books':
        book1 = command_args[1]
        book2 = command_args[2]
        if book1 in books and book2 in books:
            index_1 = books.index(book1)
            index_2 = books.index(book2)
            books[index_1], books[index_2] = books[index_2], books[index_1]

    elif action == 'Insert Book':
        name = command_args[1]
        if name not in books:
            books.append(name)

    elif action == 'Check Book':
        index = int(command_args[1])
        if is_valid_index(index, books):
            print(books[index])

    command = input()

print(', '.join(books))
