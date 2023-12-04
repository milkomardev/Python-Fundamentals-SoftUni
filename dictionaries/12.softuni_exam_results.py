line = input()

users_by_language = {}
submissions_by_language = {}

while line != 'exam finished':
    args = line.split('-')
    username = args[0]
    if args[1] == 'banned':
        for language, users in users_by_language.items():
            if username in users:
                users.pop(username)
    else:
        language = args[1]
        points = int(args[2])
        if language not in users_by_language:
            users_by_language[language] = {}

        if username in users_by_language[language]:
            users_by_language[language][username] = max(points, users_by_language[language][username])
        else:
            users_by_language[language][username] = points

        if language not in submissions_by_language:
            submissions_by_language[language] = 1
        else:
            submissions_by_language[language] += 1

    line = input()

print('Results:')
for language, students in users_by_language.items():
    for student, points in students.items():
        print(f"{student} | {points}")
print('Submissions:')
for language, submissions in submissions_by_language.items():
    print(f"{language} - {submissions}")