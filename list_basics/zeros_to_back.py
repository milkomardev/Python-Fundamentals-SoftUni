line = input().split(', ')
line_int = [int(x) for x in line]

for num in line_int:
    if num == 0:
        line_int.remove(num)
        line_int.append(num)
print(line_int)
