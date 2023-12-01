key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
special_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
forged = False

while not forged:
    line = input().lower().split()
    for idx in range(0, len(line) - 1, 2):
        quantity = int(line[idx])
        material = line[idx + 1]
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                print(f"{special_items[material]} obtained!")
                forged = True
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity

for key, value in key_materials.items():
    print(f"{key}: {value}")

for key, value in junk.items():
    print(f"{key}: {value}")
