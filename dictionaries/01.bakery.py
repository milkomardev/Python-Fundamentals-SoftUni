line = input().split()

products = {}

for idx in range(0, len(line), 2):
    product = line[idx]
    quantity = int(line[idx + 1])
    products[product] = quantity

print(products)