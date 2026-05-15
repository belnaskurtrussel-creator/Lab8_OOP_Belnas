class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_product(self, product, quantity):
        if quantity <= 0:
            print("❌ Invalid quantity.")
            return
        if product.stock >= quantity:
            product.stock -= quantity
            self.cart.append((product, quantity))
            print(f"✅ Added {quantity} x {product.name} to cart.")
        else:
            print("❌ Not enough stock.")

    def remove_product(self, product_name):
        for item in self.cart:
            if item[0].name.lower() == product_name.lower():
                product, qty = item
                product.stock += qty
                self.cart.remove(item)
                print(f"✅ Removed {product.name} from cart.")
                return
        print("❌ Product not in cart.")

    def view_cart(self):
        print("\n🛍️ Shopping Cart:")
        total = 0
        for product, qty in self.cart:
            print(f"{product.name} x{qty} - {product.price * qty:.2f}")
            total += product.price * qty
        print(f"Total Price: {total:.2f}")

# --- Demo ---
products = [
    Product("Laptop", 50000, 5),
    Product("Phone", 20000, 10),
    Product("Headphones", 2000, 15)
]

cart = ShoppingCart()
cart.add_product(products[0], 1)   # Add Laptop
cart.add_product(products[2], 2)   # Add Headphones
cart.view_cart()
cart.remove_product("Laptop")
cart.view_cart()
