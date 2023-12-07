import operator
import sys

line = input()

pass_by_contest = {}
contest_and_points_by_user = {}
while line != 'end of contests':
    contest, password = line.split(':')
    pass_by_contest[contest] = password
    line = input()

line = input()
while line != 'end of submissions':
    contest, password, username, points = line.split('=>')
    points = int(points)
    if contest in pass_by_contest:
        if password == pass_by_contest[contest]:
            if username not in contest_and_points_by_user:
                contest_and_points_by_user[username] = {}
            if username in contest_and_points_by_user and contest in contest_and_points_by_user[username]:
                contest_and_points_by_user[username][contest] = max(points,
                                                                    contest_and_points_by_user[username][contest])
            else:
                contest_and_points_by_user[username][contest] = points

    line = input()

max_total_points = 0
best_user = ''
for user, contests in contest_and_points_by_user.items():
    user_total_points = 0
    for contest, points in contests.items():
        user_total_points += points
    if user_total_points > max_total_points:
        max_total_points = user_total_points
        best_user = user
print(f"Best candidate is {best_user} with total {max_total_points} points.")
print('Ranking:')
for user, contests in sorted(contest_and_points_by_user.items()):
    print(user)
    for contest, points in sorted(contest_and_points_by_user[user].items(), key=operator.itemgetter(1), reverse=True):
        print(f"#  {contest} -> {points}")
