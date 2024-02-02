import re
text = input()
pattern = r'([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1'

matches = re.findall(pattern, text)
hidden_words = []

for match in matches:
    first_word = match[1]
    second_word = match[2]
    if first_word[::-1] == second_word:
        hidden_words.append(f"{first_word} <=> {second_word}")

if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print('No word pairs found!')

if not hidden_words:
    print('No mirror words!')
else:
    print('The mirror words are:')
    print(', '.join(hidden_words))