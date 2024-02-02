number = int(input())

cars = {}

for _ in range(number):
    line = input().split("|")
    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])
    cars[car] = {'mileage': mileage, 'fuel': fuel}

command = input()
while command != 'Stop':
    command_args = command.split(' : ')
    action = command_args[0]
    car = command_args[1]
    if action == 'Drive':
        distance = int(command_args[2])
        fuel_needed = int(command_args[3])
        if fuel_needed <= cars[car]['fuel']:
            cars[car]['mileage'] += distance
            cars[car]['fuel'] -= fuel_needed
            print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        else:
            print('Not enough fuel to make that ride')
        if cars[car]['mileage'] >= 100000:
            print(f'Time to sell the {car}!')
            cars.pop(car)

    elif action == 'Refuel':
        fuel_refill = int(command_args[2])
        old_fuel = cars[car]['fuel']
        cars[car]['fuel'] = min(75, cars[car]['fuel'] + fuel_refill)
        print(f"{car} refueled with {cars[car]['fuel'] - old_fuel} liters")

    elif action == 'Revert':
        kms = int(command_args[2])
        cars[car]['mileage'] -= kms
        if cars[car]['mileage'] >= 10000:
            print(f'{car} mileage decreased by {kms} kilometers')
        else:
            cars[car]['mileage'] = 10000

    command = input()

for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
