import math
numbers = [int(x) for x in input().split(', ')]

group_start = 1
group_end = 10

groups_count = math.ceil(max(numbers) / 10)

for index in range(1, groups_count+1):
    group_list = [x for x in numbers if group_start <= x <= group_end]
    print(f"Group of {index}0's: {group_list}")
    group_start += 10
    group_end += 10

