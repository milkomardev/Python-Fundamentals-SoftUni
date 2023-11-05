def total_price(product, quantity):
    result = 0
    if product == 'coffee':
        result = quantity * 1.50
    elif product == 'water':
        result = quantity * 1.00
    elif product == 'coke':
        result = quantity * 1.40
    elif product == 'snacks':
        result = quantity * 2.00
    return result

product = input()
quantity = int(input())

total_sum = total_price(product, quantity)

print(f'{total_sum:.2f}')
