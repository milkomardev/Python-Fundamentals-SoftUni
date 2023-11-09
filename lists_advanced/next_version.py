# version = input().split('.')
# num_as_str = ''.join(version)
# num_as_str = int(num_as_str) + 1
# num_as_str = str(num_as_str)
# print('.'.join(num_as_str))

first, second, third = [int(x) for x in input().split('.')]
third += 1

if third > 9:
    third = 0
    second += 1
    if second > 9:
        second = 0
        first += 1

print(f'{first}.{second}.{third}')
