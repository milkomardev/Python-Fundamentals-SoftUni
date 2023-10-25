decorations = int(input())
days_left = int(input())

total_cost = 0
spirit = 0

total_decorations = decorations
ornament_spirit = 5
skirt_spirit = 3
garland_spirit = 10
lights_spirit = 17

for i in range(1, days_left + 1):
    if i % 11 == 0:
        total_decorations += 2

    ornament_cost = 2 * total_decorations
    skirt_cost = 5 * total_decorations
    garland_cost = 3 * total_decorations
    lights_cost = 15 * total_decorations

    if i % 2 == 0:
        total_cost += ornament_cost
        spirit += ornament_spirit
    if i % 3 == 0:
        total_cost += skirt_cost + garland_cost
        spirit += skirt_spirit + garland_spirit
    if i % 5 == 0:
        total_cost += lights_cost
        spirit += lights_spirit
        if i % 3 == 0 and i % 5 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        total_cost += 23
    if i == days_left and i % 10 == 0:
        spirit -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit}')
