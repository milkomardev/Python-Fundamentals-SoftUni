rooms = int(input())
flag = True
free_chairs = 0
for room in range(1, rooms+1):
    chairs, visitors = input().split()
    visitors = int(visitors)
    if len(chairs) < visitors:
        print(f'{visitors - len(chairs)} more chairs needed in room {room}')
        flag = False
    else:
        free_chairs += len(chairs) - visitors

if flag:
    print(f'Game On, {free_chairs} free chairs left')