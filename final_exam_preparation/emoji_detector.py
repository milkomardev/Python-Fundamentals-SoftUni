import re
line = input()
pattern = re.compile(r'([:\*]{2})([A-Z][a-z]{2,})(\1)')
valid_emojis = list(pattern.finditer(line))
cool_threshold_sum = 1
for char in line:
    if char.isdigit():
        cool_threshold_sum *= int(char)

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")

for valid in valid_emojis:
    sum_of_ascii_letters = sum([ord(char) for char in valid[2]])
    if sum_of_ascii_letters > cool_threshold_sum:
        print(valid[0])
