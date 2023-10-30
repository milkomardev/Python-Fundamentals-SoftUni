lines = int(input())
capacity = 255

total_liters_added = 0
for n in range(lines):
    liters_added = int(input())

    if capacity >= liters_added + total_liters_added:
        total_liters_added += liters_added
    else:
        print(f'Insufficient capacity!')

print(total_liters_added)