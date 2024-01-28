import re
pattern = r'^@#+[A-Z][A-Za-z\d]{4,}[A-Z]@#+$'

number = int(input())

for _ in range(number):
    barcode = input()
    if not re.findall(pattern, barcode):
        print('Invalid barcode')
        continue
    else:
        digits = re.findall(r"\d", barcode)
        if not digits:
            print(f'Product group: 00')
        else:
            print(f"Product group: {''.join(digits)}")