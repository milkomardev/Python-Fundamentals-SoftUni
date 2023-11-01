red_cards = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

terminated = False

for idx in red_cards:
    cards = idx.split('-')
    team = cards[0]
    player = int(cards[1])
    if team == 'A' and player in team_a:
        team_a.remove(player)
    elif team == 'B' and player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        terminated = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if terminated:
    print('Game was terminated')
