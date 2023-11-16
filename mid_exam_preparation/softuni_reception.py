first = int(input())
second = int(input())
third = int(input())
students = int(input())

total_per_hour = first + second + third
hours = 1
students_left = students
while students_left >= 0:
    if students_left == 0:
        hours = 0
        break
    if hours % 4 == 0:
        hours += 1
        continue
    else:
        students_left -= min(total_per_hour, students_left)
        if students_left == 0:
            break
        hours += 1

print(f'Time needed: {hours}h.')
