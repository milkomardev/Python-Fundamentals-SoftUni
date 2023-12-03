line = input().lower().split()
occurrences = {}

for word in line:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

for key, value in occurrences.items():
    if value % 2 != 0:
        print(key, end=' ')

