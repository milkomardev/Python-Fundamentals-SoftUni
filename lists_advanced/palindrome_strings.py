line = input().split()
given_word = input()
palindromes = []
given_word_counter = 0
for word in line:
    if word == ''.join(reversed(word)):
        palindromes.append(word)
        if word == given_word:
            given_word_counter += 1

print(palindromes)
print(f'Found palindrome {given_word_counter} times')
