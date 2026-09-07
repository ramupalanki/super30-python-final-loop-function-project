"""Simple Shopping Cart Application."""

def add_product(cart):
    """Add a product and quantity to the cart."""
    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))
        if price < 0 or quantity <= 0:
            print("Price must be non-negative and quantity must be positive.")
            return

        if name in cart:
            cart[name]["quantity"] += quantity
            cart[name]["price"] = price
        else:
            cart[name] = {"price": price, "quantity": quantity}
        print("Product added to cart.")
    except ValueError:
        print("Please enter valid values.")


def remove_product(cart):
    """Remove a product from the cart."""
    name = input("Enter product name to remove: ").strip()
    if name in cart:
        del cart[name]
        print("Product removed.")
    else:
        print("Product not found in cart.")


def view_cart(cart):
    """Display the current cart."""
    print("\n===== SHOPPING CART =====")
    if not cart:
        print("Cart is empty.")
        return

    for name, item in cart.items():
        value = item["price"] * item["quantity"]
        print(
            f"{name} | Price: {item['price']:.2f} | "
            f"Quantity: {item['quantity']} | Total: {value:.2f}"
        )


def calculate_bill(cart):
    """Calculate and display the total bill."""
    total = 0
    for item in cart.values():
        total += item["price"] * item["quantity"]
    print(f"Total bill: {total:.2f}")
    return total


def main():
    """Run the shopping cart application."""
    cart = {}

    while True:
        print("\n===== SHOPPING CART =====")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Calculate Bill")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_product(cart)
        elif choice == "2":
            remove_product(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            calculate_bill(cart)
        elif choice == "5":
            print("Thank you for shopping.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
