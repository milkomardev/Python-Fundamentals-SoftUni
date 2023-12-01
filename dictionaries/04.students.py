line = input()

courses = {}
while ':' in line:
    name, ID, course = line.split(':')
    ID = int(ID)

    if course not in courses:
        courses[course] = {}

    courses[course][name] = ID
    line = input()

line = line.split('_')
line = ' '.join(line)

if line in courses:
    for key, value in courses[line].items():
        print(f"{key} - {value}")
        