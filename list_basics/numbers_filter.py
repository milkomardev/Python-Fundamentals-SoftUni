n = int(input())

even_nums = []
odd_nums = []
positive_nums = []
negative_nums = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_nums.append(number)
    elif number < 0:
        negative_nums.append(number)
    if number % 2 == 0:
        even_nums.append(number)
    else:
        odd_nums.append(number)

command = input()

if command == 'even':
    print(even_nums)
elif command == 'odd':
    print(odd_nums)
elif command == 'positive':
    print(positive_nums)
else:
    print(negative_nums)
