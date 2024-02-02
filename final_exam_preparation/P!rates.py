line = input()

cities = {}

while line != "Sail":
    args_line = line.split('||')
    city = args_line[0]
    population = int(args_line[1])
    gold = int(args_line[2])
    if city not in cities:
        cities[city] = {'population':population, 'gold':gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

    line = input()

line = input()

while line != 'End':
    args_line = line.split('=>')
    command = args_line[0]
    city = args_line[1]
    if command == 'Plunder':
        people = int(args_line[2])
        gold = int(args_line[3])
        cities[city]['population'] -= people
        cities[city]['gold'] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            cities.pop(city)
            print(f"{city} has been wiped off the map!")
    else:
        gold = int(args_line[2])
        if gold >= 0:
            cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")
    line = input()

if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    for city in cities:
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')