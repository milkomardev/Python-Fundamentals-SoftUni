first = ord(input())
second = ord(input())

line = input()
score = 0
for ch in line:
    if first < ord(ch) < second:
        score += ord(ch)
print(score)