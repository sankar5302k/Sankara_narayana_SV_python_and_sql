class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

class Perishable(Product):
    pass

class Electronics(Product):
    pass

class InventoryManager:
    def __init__(self):
        self.inventory = {}
        self.low_stock_threshold = 5

    def add_product(self, product):
        self.inventory[product.name] = product

    def print_summary(self):
        low_stock_alerts = set()
        print("Inventory Summary:")
        for name, prod in self.inventory.items():
            print(f"- {name}: {prod.stock}")
            if prod.stock < self.low_stock_threshold:
                low_stock_alerts.add(name)
        
        if low_stock_alerts:
            print(f"Low Stock Alerts: {', '.join(low_stock_alerts)}")

im = InventoryManager()
im.add_product(Perishable("Apples", 50))
im.add_product(Electronics("Laptops", 2))
im.print_summary()
