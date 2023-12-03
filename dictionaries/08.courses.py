courses = {}
line = input()

while line != 'end':
    course, student = line.split(' : ')
    if course not in courses:
        courses[course] = []
    courses[course].append(student)
    line = input()

for course, students in courses.items():
    print(f"{course}: {len(courses[course])}")
    for student in students:
        print(f"-- {student}")
