number = int(input())

for n in range(number):
    line = input()
    is_pure = True
    for ch in line:
        if ch in [',', '.', '_']:
            is_pure = False
            break
    if is_pure:
        print(f'{line} is pure.')
    else:
        print(f'{line} is not pure!')
