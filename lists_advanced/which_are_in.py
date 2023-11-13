sub_strings = input().split(', ')
strings = input().split(', ')
filtered = []

for sub_str in sub_strings:
    for string in strings:
        if sub_str in string:
            filtered.append(sub_str)
            break

print(filtered)
