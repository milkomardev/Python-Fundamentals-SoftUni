population = [int(x) for x in input().split(', ')]
min_wealth = int(input())

for person_wealth in range(len(population)):
    max_wealth = max(population)
    if max_wealth <= min_wealth:
        break

    poor = min(population)

    idx_max_wealth = population.index(max_wealth)
    idx_poor = population.index(poor)

    transfer = min_wealth - poor
    if transfer == 0:
        continue

    population[idx_poor] += transfer
    population[idx_max_wealth] -= transfer

if min(population) < min_wealth:
    print('No equal distribution possible')
else:
    print(population)
