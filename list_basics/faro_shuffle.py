deck = input().split()
shuffle_count = int(input())

for _ in range(shuffle_count):
    first_half = []
    second_half = []
    for idx in range(len(deck)):
        card = deck[idx]
        if idx < len(deck) / 2:
            first_half.append(card)
        else:
            second_half.append(card)

    result = []
    first_part_index = 0
    second_part_index = 0
    for idx in range(len(first_half) * 2):
        if idx % 2 == 0:
            result.append(first_half[first_part_index])
            first_part_index += 1
        else:
            result.append((second_half[second_part_index]))
            second_part_index += 1
    deck = result

print(deck)


