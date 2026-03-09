# ByteBites Models
#
# Classes:
#   - Customer   : a registered user with a name and order history
#   - MenuItem   : a single food/drink item with name, price, category, and rating
#   - Menu       : the full catalog of items; supports filtering by category
#   - Order      : a transaction grouping selected items; computes the total cost


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return f"MenuItem({self.name!r}, ${self.price:.2f}, {self.category!r}, rating={self.popularity_rating})"


class Order:
    def __init__(self):
        self.items: list = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def compute_total(self) -> float:
        return sum(item.price for item in self.items)

    def __repr__(self):
        return f"Order(items={self.items}, total=${self.compute_total():.2f})"


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history: list = []

    def add_order(self, order: Order):
        self.purchase_history.append(order)

    def verify_user(self) -> bool:
        return len(self.purchase_history) > 0

    def __repr__(self):
        return f"Customer({self.name!r}, orders={len(self.purchase_history)})"


class Menu:
    def __init__(self):
        self.items: list = []

    def add_item(self, item: MenuItem):
        self.items.append(item)

    def filter_by_category(self, category: str) -> list:
        return [item for item in self.items if item.category == category]

    def __repr__(self):
        return f"Menu(items={len(self.items)})"


# --- Quick manual check ---
if __name__ == "__main__":
    burger = MenuItem("Spicy Burger", 8.99, "Burgers", 4.5)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 4.0)
    cake = MenuItem("Chocolate Cake", 4.99, "Desserts", 4.8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    print("Full menu:", menu)
    print("Drinks:", menu.filter_by_category("Drinks"))

    order = Order()
    order.add_item(burger)
    order.add_item(soda)
    print("Order:", order)

    customer = Customer("Jorge")
    print("Verified before order:", customer.verify_user())
    customer.add_order(order)
    print("Verified after order:", customer.verify_user())
    print("Customer:", customer)
