capacity = int(input())
users = {}
command = input()

while command != "Statistics":
    command = command.split('=')
    action = command[0]

    if action == 'Add':
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in users:
            users[username] = {'sent': sent, 'received': received}

    elif action == 'Message':
        sender = command[1]
        receiver = command[2]
        if sender in users and receiver in users:
            users[sender]['sent'] += 1
            if users[sender]['sent'] + users[sender]['received'] == capacity:
                users.pop(sender)
                print(f"{sender} reached the capacity!")

            users[receiver]['received'] += 1
            if users[receiver]['sent'] + users[receiver]['received'] == capacity:
                users.pop(receiver)
                print(f"{receiver} reached the capacity!")

    elif action == 'Empty':
        username = command[1]
        if username == 'All':
            users.clear()
        else:
            users.pop(username)

    command = input()

print(f"Users count: {len(users)}")

for user in users:
    print(f"{user} - {users[user]['sent'] + users[user]['received']}")