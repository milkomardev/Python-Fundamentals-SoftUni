numbers = [int(x) for x in input().split()]
numbers.sort()
avg_number = sum(numbers) / len(numbers)
higher_than_avg = [x for x in numbers if x > avg_number]
higher_than_avg.sort(reverse=True)
result = []
is_avg_numbers = True

if len(higher_than_avg) >= 5:
    for n in range(5):
        result.append(higher_than_avg[n])
elif len(higher_than_avg) == 0:
    print('No')
    is_avg_numbers = False
else:
    for n in range(len(higher_than_avg)):
        result.append(higher_than_avg[n])

if is_avg_numbers:
    result_as_str = [str(x) for x in result]
    print(' '.join(result_as_str))






