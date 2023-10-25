number = int(input())
total_price = 0

for n in range(number):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if not 0.01 <= capsule_price <= 100.00:
        continue
    elif not 1 <= days <= 31:
        continue
    elif not 1 <= capsules_per_day <= 2000:
        continue
    price = days * capsule_price * capsules_per_day
    print(f'The price for the coffee is: ${price:.2f}')
    total_price += price

print(f'Total: ${total_price:.2f}')