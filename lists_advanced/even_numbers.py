numbers = [int(x) for x in input().split(', ')]
index_list = []

print([index for index in range(len(numbers)) if numbers[index] % 2 == 0])

# for num in range(len(numbers)):
#     if num % 2 == 0:
#         index_list.append(numbers[num])
