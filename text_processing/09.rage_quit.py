line = input()

result = ""
current_str = ''

for ch in range(len(line)):
    if ch + 1 < len(line) and line[ch].isdigit() and line[ch+1].isdigit():
        multiplier = int(line[ch:ch+2])
        result += multiplier * current_str
        current_str = ''
    elif line[ch].isdigit():
        multiplier = int(line[ch])
        result += multiplier * current_str
        current_str = ''
    else:
        current_str += line[ch].upper()

symbols = set(result)

print(f"Unique symbols used: {len(symbols)}")
print(result)