def get_min_number(nums):
    return min(nums)


def get_max_number(nums):
    return max(nums)


def sum_numbers(nums):
    return sum(nums)


numbers = [int(x) for x in input().split()]

print(f'The minimum number is {get_min_number(numbers)}')
print(f'The maximum number is {get_max_number(numbers)}')
print(f'The sum number is: {sum_numbers(numbers)}')