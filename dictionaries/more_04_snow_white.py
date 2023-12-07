line = input()
dwarfs = {}

while line != 'Once upon a time':
    name, hat, physics = line.split(' <:> ')
    physics = int(physics)
    if name not in dwarfs:
        dwarfs[name] = {}
    if hat not in dwarfs[name]:
        dwarfs[name][hat] = physics
    else:
        dwarfs[name][hat] = max(dwarfs[name][hat], physics)

    line = input()

for dwarf, hats in sorted(dwarfs.items(), key=lambda x: (-len(x[1].values()), x[0])):
    for hat, physics in sorted(hats.items(), key=lambda x: (-x[1], x[0])):
        print(f"({hat}) {dwarf} <-> {physics}")