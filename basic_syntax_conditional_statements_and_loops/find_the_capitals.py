word = input()

list_of_caps = []

for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        list_of_caps.append(i)

print(list_of_caps)