def is_valid_piece(piece, list):
    return piece in list


number = int(input())

pieces = {}

for _ in range(number):
    line_args = input().split('|')
    piece = line_args[0]
    composer = line_args[1]
    key = line_args[2]
    pieces[piece] = {'composer': composer, 'key': key}

command = input()
while command != 'Stop':
    cmd_args = command.split('|')
    action = cmd_args[0]
    piece = cmd_args[1]
    if action == 'Add':
        composer = cmd_args[2]
        key = cmd_args[3]
        if is_valid_piece(piece, pieces):
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == 'Remove':
        if is_valid_piece(piece, pieces):
            print(f"Successfully removed {piece}!")
            pieces.pop(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == 'ChangeKey':
        new_key = cmd_args[2]
        if is_valid_piece(piece, pieces):
            pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece in pieces:
    print(f"{piece} -> Composer: {pieces[piece]['composer']}, Key: {pieces[piece]['key']}")