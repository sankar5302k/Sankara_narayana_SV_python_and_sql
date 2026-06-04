import math

class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [i for i in self.items if i.name != item_name]

    def calculate_total(self):
        return sum(item.price * item.quantity for item in self.items)

cart = ShoppingCart()

cart.add_item(CartItem("Laptop", 1000, 1))
cart.add_item(CartItem("Mouse", 50, 2))

subtotal = cart.calculate_total()
gst = subtotal * 0.18
total = subtotal + gst
total = math.ceil(total * 100) / 100

print("RECEIPT:")
for item in cart.items:
    print(f"{item.name} x {item.quantity} = ${item.price * item.quantity:.2f}")

print(f"\nSubtotal: ${subtotal:.2f}")
print(f"GST (18%): ${gst:.2f}")
print(f"Final Total: ${total:.2f}")

