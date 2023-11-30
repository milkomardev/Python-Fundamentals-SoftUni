line = input().split()

products = {}

for idx in range(0, len(line), 2):
    product = line[idx]
    quantity = int(line[idx + 1])
    products[product] = quantity


needed_products = input().split()

for product in needed_products:
    if product in products:
        print(f'We have {products[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")