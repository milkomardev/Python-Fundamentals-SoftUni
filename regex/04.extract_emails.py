import re
text = input()
pattern = r"\s([A-Za-z][A-Za-z\d\.\-_]*[A-Za-z]@[A-Za-z\-]+(\.[A-Za-z-]+)+)"
matches = re.findall(pattern, text)

for match in matches:
    print(match[0])
