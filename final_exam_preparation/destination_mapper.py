import re
line = input()
pattern = r'([=/])([A-Z][A-Za-z]{2,})\1'
total_length = 0

matches = re.finditer(pattern, line)

destinations = []
for match in matches:
    total_length += len(match[2])
    destinations.append(match.group(2))

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_length}")