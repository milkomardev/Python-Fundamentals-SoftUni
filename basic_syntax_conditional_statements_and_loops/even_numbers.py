n = int(input())
flag = True

for i in range(n):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        flag = False
        break
    else:
        continue

if flag:
    print('All numbers are even.')