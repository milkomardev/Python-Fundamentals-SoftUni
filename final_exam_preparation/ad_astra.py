import re
line = input()
total_calories = 0
pattern = r'([#|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'

matches = re.findall(pattern, line)

for match in matches:
    total_calories += int(match[3])

days_to_last = total_calories // 2000

print(f"You have food to last you for: {days_to_last} days!")

for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")