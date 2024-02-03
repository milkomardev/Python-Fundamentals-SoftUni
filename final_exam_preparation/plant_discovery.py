def is_valid_plant(plant,plants):
    return plant in plants


number = int(input())
rarity_by_plant = {}
rating_by_plant = {}

for _ in range(number):
    line = input().split('<->')
    plant = line[0]
    rarity = int(line[1])
    rarity_by_plant[plant] = rarity
    rating_by_plant[plant] = []

command = input()

while command != 'Exhibition':
    cmd_args = command.split(': ')
    action = cmd_args[0]
    plant_args = cmd_args[1].split(' - ')
    plant = plant_args[0]

    if is_valid_plant(plant, rarity_by_plant):
        if action == 'Rate':
            rating = int(plant_args[1])
            rating_by_plant[plant].append(rating)

        elif action == 'Update':
            new_rarity = int(plant_args[1])
            rarity_by_plant[plant] = new_rarity

        elif action == 'Reset':
            rating_by_plant[plant].clear()

    else:
        print('error')
    command = input()

print('Plants for the exhibition:')
for plant in rarity_by_plant:
    avg_rating = len(rating_by_plant[plant])
    if avg_rating > 0:
        avg_rating = sum(rating_by_plant[plant]) / avg_rating
    print(f"- {plant}; Rarity: {rarity_by_plant[plant]}; Rating: {avg_rating:.2f}")
