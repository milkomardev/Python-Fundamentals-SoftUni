text = input()
vowels = ['a', 'o', 'u', 'e', 'i']

print(''.join([char for char in text if not char.lower() in vowels]))

# print([char for char in input() if not char.lower() in ['a', 'o', 'u', 'e', 'i']])

