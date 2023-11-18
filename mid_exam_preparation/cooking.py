import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())

total_flour = flour_price * (students - (students // 5))
total_egg_price = students * 10 * egg_price
total_aprons = (apron_price * math.ceil(students * 1.20))

total_price = total_egg_price + total_aprons + total_flour

if total_price <= budget:
    print(f'Items purchased for {total_price:.2f}$.')
else:
    diff = total_price - budget
    print(f'{diff:.2f}$ more needed.')
