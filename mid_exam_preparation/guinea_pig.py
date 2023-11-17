food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
is_enough = True

for day in range(1, 31):
    food -= 300
    if day % 2 == 0:
        hay -= round((food * 0.05), 2)
    if day % 3 == 0:
        cover -= round((weight / 3), 2)
    if food <= 0 or hay <= 0 or cover <= 0:
        print('Merry must go to the pet store!')
        is_enough = False
        break

if is_enough:
    print(f'Everything is fine! Puppy is happy! Food: {food/1000:.2f}, Hay: {hay/1000:.2f}, Cover: {cover/1000:.2f}.')
