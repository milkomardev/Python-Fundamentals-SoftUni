text = input().split()
result = []
for word in text:
    word_as_list = list(word)
    first_letter = ''
    counter = 0
    for letter in word:
        if letter.isdigit():
            first_letter += letter
            counter += 1
    first_letter = int(first_letter)
    [word_as_list.pop(0) for x in range(counter)]
    word_as_list.insert(0, chr(first_letter))
    word_as_list[1], word_as_list[-1] = word_as_list[-1], word_as_list[1]
    result.append(''.join(word_as_list))

print(' '.join(result))
