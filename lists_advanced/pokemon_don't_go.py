sequence = [int(x) for x in input().split()]

sum_of_removed = 0
while len(sequence) > 0:
    index = int(input())
    index_sum = 0
    flag = True
    sum_removed = False
    if index < 0:
        index_sum = sequence[0]
        sum_of_removed += index_sum
        sequence[0] = sequence[-1]
        flag = False
        sum_removed = True
    elif index > len(sequence) - 1:
        index_sum = sequence[-1]
        sum_of_removed += index_sum
        sequence[-1] = sequence[0]
        flag = False
        sum_removed = True
    else:
        index_sum = sequence[index]

    for element in range(len(sequence)):
        if sequence[element] == index_sum and not sum_removed:
            sum_of_removed += index_sum
        elif sequence[element] <= index_sum:
            sequence[element] += index_sum
        else:
            sequence[element] -= index_sum

    if flag:
        sequence.pop(index)
print(sum_of_removed)
