import re

pattern = r">>(?P<type>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
bought_furniture = []
total_spent = 0

while True:
    line = input()
    if line == 'Purchase':
        break

    match = re.match(pattern, line)
    if not match:
        continue

    groups = match.groupdict()
    bought_furniture.append(groups['type'])
    total_spent += float(groups['price']) * int(groups['quantity'])

print('Bought furniture:')
for item in bought_furniture:
    print(item)
print(f'Total money spend: {total_spent:.2f}')
