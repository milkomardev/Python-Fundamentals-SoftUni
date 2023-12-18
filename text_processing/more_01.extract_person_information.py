number = int(input())

for _ in range(number):
    line = input().split()
    name = ''
    age = 0
    for part in line:
        if "@" in part and '|' in part:
            if part.index('@') < part.index('|'):
                name = part[part.index('@') + 1: part.index('|')]

        if "#" in part and '*' in part:
            if part.index('#') < part.index('*'):
                age = int(part[part.index('#') + 1: part.index('*')])

    print(f"{name} is {age} years old.")