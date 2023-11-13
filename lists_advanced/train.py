wagons = int(input())
train = [0] * wagons
command = input()

while command != "End":
    action = command.split()
    if action[0] == 'add':
        train[-1] += int(action[1])
    elif action[0] == 'insert':
        index = int(action[1])
        people = int(action[2])
        train[index] += people
    elif action[0] == 'leave':
        index = int(action[1])
        people = int(action[2])
        train[index] -= people

    command = input()

print(train)