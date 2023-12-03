count = int(input())
users = {}

for _ in range(count):
    line = input()
    args = line.split()
    command = args[0]
    name = args[1]
    if command == 'register':
        plate = args[2]
        if name not in users:
            users[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {users[name]}")
    else:
        if name not in users:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            users.pop(name)

for user, plate in users.items():
    print(f"{user} => {plate}")