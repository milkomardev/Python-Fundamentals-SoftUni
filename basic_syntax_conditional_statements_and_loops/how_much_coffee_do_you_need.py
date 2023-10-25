command = input()
total_coffees = 0
while command != 'END':
    if command in ['coding', 'cat', 'dog', 'movie']:
        total_coffees += 1
    elif command in ['CODING', 'CAT', 'DOG', 'MOVIE']:
        total_coffees += 2
    else:
        command = input()
        continue
    command = input()

if total_coffees > 5:
    print('You need extra sleep')
else:
    print(total_coffees)