def is_valid_index(index, sequence):
    return 0 <= index < len(sequence)


def is_shot_target(index):
    return index == -1


targets = [int(x) for x in input().split()]
count = 0
command = input()

while command != 'End':
    index = int(command)
    if not is_valid_index(index, targets):
        command = input()
        continue
    for num in range(len(targets)):
        if is_shot_target(targets[num]):
            continue
        if num == index:
            count += 1
            for target in range(len(targets)):
                if targets[target] > targets[num]:
                    targets[target] -= targets[num]
                elif targets[target] == -1:
                    continue
                elif target == num:
                    continue
                else:
                    targets[target] += targets[num]
            targets[num] = -1
            break
    command = input()

targets = [str(x) for x in targets]

print(f"Shot targets: {count} -> {' '.join(targets)}")