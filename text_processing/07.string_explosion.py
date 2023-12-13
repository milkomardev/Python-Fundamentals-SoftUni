line = input()
parts = line.split('>')
result = [parts[0]]
previous = 0

for part in parts[1:]:
    power = int(part[0])
    previous += power
    formatted_part = part[previous:]
    previous = max(0, previous - len(part))
    result.append(formatted_part)

print('>'.join(result))

