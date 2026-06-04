def create_shopping_cart():
    cart = [100, 250, 75]
    if not all(isinstance(item, (int, float)) and item >= 0 for item in cart):
        print("Invalid items in cart")
        return
    print(f"Shopping Cart: {cart}")

create_shopping_cart()
