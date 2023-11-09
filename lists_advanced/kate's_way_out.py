rows = int(input())
moves_count = 0
got_out = True

for row in range(rows):
    moves = list(input())
    if 'k' in moves:
        start_row = row
    if ' ' in moves:
        steps = moves.count(' ')
        moves_count += steps
    if row > 0 and ' ' not in moves:
        got_out = False
        print('Kate cannot get out')

moves_count += 1
if got_out:
    print(f'Kate got out in {moves_count} moves')