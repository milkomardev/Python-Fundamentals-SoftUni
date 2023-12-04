line = input()

users_by_force = {}
force_by_user = {}

while line != 'Lumpawaroo':
    if " | " in line:
        side, user = line.split(' | ')
        if side not in users_by_force:
            users_by_force[side] = []
        if user not in force_by_user:
            force_by_user[user] = side
            users_by_force[side].append(user)

    elif " -> " in line:
        user, side = line.split(' -> ')
        if side not in users_by_force:
            users_by_force[side] = []
        if user in force_by_user:
            old_side = force_by_user[user]
            force_by_user[user] = side
            users_by_force[old_side].remove(user)
            users_by_force[side].append(user)
        else:
            force_by_user[user] = side
            users_by_force[side].append(user)
        print(f"{user} joins the {side} side!")

    line = input()

for side, users in users_by_force.items():
    if len(users) != 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
