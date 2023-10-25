animals = input()

list_of_animals = animals.split(', ')

for i in range(len(list_of_animals)-1, -1, -1):
    if list_of_animals[i] == 'wolf':
        if i == len(list_of_animals) - 1:
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {len(list_of_animals)- (i + 1)}! You are about to be eaten by a wolf!')
