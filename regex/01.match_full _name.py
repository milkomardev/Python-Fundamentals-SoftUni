import re
line = input()
pattern = r'(\b[A-Z][a-z]+ [A-Z][a-z]+\b)'
matches = re.findall(pattern, line)
print(' '.join(matches))
