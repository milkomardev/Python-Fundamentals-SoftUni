line = input()
filtered = line[0]
for ch in line:
    if ch != filtered[-1]:
        filtered += ch
print(filtered)
