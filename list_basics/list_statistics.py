lines = int(input())

positives_list = []
positives_count = 0
negatives_list = []


for _ in range(lines):
    n = int(input())
    if n >= 0:
        positives_list.append(n)
        positives_count += 1
    elif n < 0:
        negatives_list.append(n)

print(positives_list)
print(negatives_list)
print(f'Count of positives: {positives_count}')
print(f'Sum of negatives: {sum(negatives_list)}')