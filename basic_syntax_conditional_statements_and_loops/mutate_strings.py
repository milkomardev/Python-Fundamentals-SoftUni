first_word = input()
second_word = input()

result = first_word

for idx in range(len(first_word)):
    if first_word[idx] == second_word[idx]:
        continue
    result = second_word[:idx + 1] + first_word[idx + 1:]

    print(result)