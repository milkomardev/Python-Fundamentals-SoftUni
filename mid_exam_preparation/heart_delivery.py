neighbourhood = [int(x) for x in input().split('@')]
command = input()
current_index = 0
while command != 'Love!':
    command_args = command.split()
    index = int(command_args[1])
    if current_index + index >= len(neighbourhood):
        current_index = 0
        index = 0
    if neighbourhood[current_index + index] == 0:
        print(f"Place {current_index + index} already had Valentine's day.")
        current_index = current_index + index
        command = input()
        continue
    neighbourhood[current_index + index] -= 2
    if neighbourhood[current_index + index] == 0:
        print(f"Place {current_index + index} has Valentine's day.")
    current_index = current_index + index

    command = input()

print(f"Cupid's last position was {current_index}.")
counter = 0
for house in neighbourhood:
    if house > 0:
        counter += 1

if sum(neighbourhood) == 0:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {counter} places.')