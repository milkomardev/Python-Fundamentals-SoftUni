fire = input().split('#')
water = int(input())

total_effort = 0
cells = []
total_fire = 0
for idx in fire:
    fire_args = idx.split(' = ')
    type_of_fire = fire_args[0]
    value = int(fire_args[1])

    if type_of_fire == 'High' and (value < 81 or value > 125):
        continue

    if type_of_fire == 'Medium' and (value < 51 or value > 80):
        continue

    if type_of_fire == 'Low' and (value < 1 or value > 50):
        continue

    if value > water:
        continue

    water -= value
    effort = value * 0.25
    total_effort += effort
    cells.append(value)
    total_fire += value

print('Cells: ')
for index in cells:
    print(f' - {index}')
print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')