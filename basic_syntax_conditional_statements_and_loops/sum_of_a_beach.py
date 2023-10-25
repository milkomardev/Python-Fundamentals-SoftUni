string = input().lower()
counter = 0

words = ['water', 'sand', 'fish', 'sun']

for word in words:
    if word in string:
        counter += 1

print(counter)