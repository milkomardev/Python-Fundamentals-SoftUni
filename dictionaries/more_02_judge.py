line = input()

users_by_contest = {}
total_points_by_user = {}

while line != 'no more time':
    username, contest, points = line.split(' -> ')
    points = int(points)
    if contest not in users_by_contest:
        users_by_contest[contest] = {}
    if username in users_by_contest[contest]:
        users_by_contest[contest][username] = max(points, users_by_contest[contest][username])
    else:
        users_by_contest[contest][username] = points

    line = input()

for contest, users in users_by_contest.items():
    for user, points in users.items():
        if user not in total_points_by_user:
            total_points_by_user[user] = 0
        total_points_by_user[user] += points

for contest, users in users_by_contest.items():
    print(f"{contest}: {len(users)} participants")
    count = 1
    for user, points in sorted(users.items(), key=lambda x: (-x[1], x[0])):
        print(f"{count}. {user} <::> {points}")
        count += 1

print(f"Individual standings:")
count = 1
for user, points in sorted(total_points_by_user.items(), key=lambda x: (-x[1], x[0])):
    print(f"{count}. {user} -> {points}")
    count += 1
