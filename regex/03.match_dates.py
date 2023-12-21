import re
text = input()
pattern = r"\b(?P<day>[\d]{2})([\.\-/])(?P<month>[A-Z][a-z]{2})\2(?P<year>[\d]{4})\b"
dates = re.findall(pattern, text)

for date in dates:
    day = date[0]
    month = date[2]
    year = date[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')