first, second = input().split()
min_len = min(len(first), len(second))
result = 0

for n in range(min_len):
    result += ord(first[n]) * ord(second[n])

for ch in range(min_len, len(first)):
    result += ord(first[ch])

for ch in range(min_len, len(second)):
    result += ord(second[ch])

print(result)