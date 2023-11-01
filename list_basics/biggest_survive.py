numbers = [int(x) for x in input().split()]
count = int(input())

for num in range(count):
    numbers.remove(min(numbers))

numbers_in_str = [str(x) for x in numbers]
result = ", ".join(numbers_in_str)

print(result)