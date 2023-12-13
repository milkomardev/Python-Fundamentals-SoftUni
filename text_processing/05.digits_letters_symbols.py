digits = []
letters = []
symbols = []

line = input()

for char in line:
    if char.isdigit():
        digits.append(char)
    elif char.isalpha():
        letters.append(char)
    else:
        symbols.append(char)

print(''.join(digits))
print(''.join(letters))
print(''.join(symbols))