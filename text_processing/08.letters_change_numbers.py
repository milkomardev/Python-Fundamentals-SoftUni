line = input().split()
result = 0

for part in line:
    part.strip()
    number = int(part[1:-1])

    if part[0].isupper():
        number /= ord(part[0].lower()) - 96
    else:
        number *= ord(part[0].lower()) - 96

    if part[-1].isupper():
        number -= ord(part[-1].lower()) - 96
    else:
        number += ord(part[-1].lower()) - 96

    result += number

print(f"{result:.2f}")

