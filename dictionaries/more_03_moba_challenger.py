pos_skill_by_player = {}
line = input()

while line != 'Season end':
    if ' -> ' in line:
        player, position, skill = line.split(' -> ')
        skill = int(skill)
        if player not in pos_skill_by_player:
            pos_skill_by_player[player] = {}

        if position in pos_skill_by_player[player]:
            pos_skill_by_player[player][position] = max(skill, pos_skill_by_player[player][position])
        else:
            pos_skill_by_player[player][position] = skill
    else:
        player_1, player_2 = line.split(' vs ')
        if player_1 in pos_skill_by_player and player_2 in pos_skill_by_player:
            for position in pos_skill_by_player[player_1]:
                if position in pos_skill_by_player[player_2]:
                    player_1_max = sum(pos_skill_by_player[player_1].values())
                    player_2_max = sum(pos_skill_by_player[player_2].values())
                    if player_1_max > player_2_max:
                        pos_skill_by_player.pop(player_2)
                        break
                    elif player_2_max > player_1_max:
                        pos_skill_by_player.pop(player_1)
                        break
    line = input()

for player, positions in sorted(pos_skill_by_player.items(), key=lambda x: (-sum(x[1].values()), (x[0]))):
    print(f"{player}: {sum(pos_skill_by_player[player].values())} skill")
    for position, skill in sorted(pos_skill_by_player[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")
