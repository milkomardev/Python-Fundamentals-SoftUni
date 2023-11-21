class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, name):
        self.products.append(name)

    def get_by_letter(self, first_letter):
        filtered = [product for product in self.products if product[0] == first_letter]
        return filtered

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:"
        for product in sorted(self.products):
            result += '\n' + product
        return result

catalogue = Catalogue("My Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
