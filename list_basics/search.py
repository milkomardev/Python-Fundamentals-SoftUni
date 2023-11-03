number = int(input())
word = input()

all_strings = []
strings_with_word = []
for _ in range(number):
    current_string = input()
    all_strings.append(current_string)
    if word in current_string:
        strings_with_word.append(current_string)

print(all_strings)
print(strings_with_word)
