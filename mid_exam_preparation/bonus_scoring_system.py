from math import ceil

students = int(input())
total_lectures = int(input())
bonus = int(input())

max_bonus = 0
max_lectures = 0

for student in range(students):
    lectures_attended = int(input())
    if total_lectures == 0:
        break
    total_bonus = (lectures_attended / total_lectures) * (5 + bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_lectures = lectures_attended

print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {max_lectures} lectures.')