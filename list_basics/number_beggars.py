numbers = [int(x) for x in input().split(', ')]
count = int(input())

beggars = [0] * count

for i in range(len(numbers)):
    beggars_idx = i % count
    num = numbers[i]
    beggars[beggars_idx] += num

print(beggars)

