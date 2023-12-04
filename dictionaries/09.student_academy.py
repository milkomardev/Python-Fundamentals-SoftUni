rows = int(input())
students = {}

for row in range(rows):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grade in students.items():
    avg_grade = sum(grade) / len(grade)
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")
