numbers = [int(x) for x in input().split()]

left_time = 0
right_time = 0

for left in range(0, int(len(numbers)/2)):
    if numbers[left] != 0:
        left_time += numbers[left]
    elif numbers[left] == 0:
        left_time = left_time * 0.8

for right in range(len(numbers) - 1, int(len(numbers)/2), -1):
    if numbers[right] != 0:
        right_time += numbers[right]
    elif numbers[right] == 0:
        right_time = right_time * 0.8

if left_time < right_time:
    print(f'The winner is left with total time: {left_time:.1f}')
else:
    print(f'The winner is right with total time: {right_time:.1f}')
