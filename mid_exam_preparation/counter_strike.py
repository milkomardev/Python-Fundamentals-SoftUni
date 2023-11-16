energy = int(input())
command = input()
battles_won = 0
no_energy = False

while command != 'End of battle':
    distance = int(command)
    if energy < distance:
        print(f'Not enough energy! Game ends with {battles_won} won battles and {energy} energy')
        no_energy = True
        break
    else:
        energy -= distance
        battles_won += 1
        if battles_won % 3 == 0:
            energy += battles_won

    command = input()

if not no_energy:
    print(f'Won battles: {battles_won}. Energy left: {energy}')