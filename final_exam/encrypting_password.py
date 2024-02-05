import re
n = int(input())
pattern = r'^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

for _ in range(n):
    password = input()
    if not re.findall(pattern, password):
        print(f"Try another password!")
    else:
        groups = re.finditer(pattern,password)
        for group in groups:
            print(f"Password: {group[2] + group[3] + group[4] + group[5]}")