class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.capacity_left = self.__capacity

    def add_item(self, item):
        if self.capacity_left == 0:
            return "not enough room in the inventory"
        self.items.append(item)
        self.capacity_left -= 1

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity_left}"

inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

