line = input()
phonebook = {}
while '-' in line:
    name, number = line.split('-')
    phonebook[name] = number
    line = input()

for n in range(int(line)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f'Contact {name} does not exist.')