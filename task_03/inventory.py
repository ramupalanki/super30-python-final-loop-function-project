"""Inventory Management System."""

def add_product(products):
    """Add a new product to the inventory."""
    name = input("Enter product name: ").strip()
    if not name:
        print("Product name cannot be empty.")
        return

    try:
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            return
        products[name] = {"price": price, "quantity": quantity}
        print("Product added successfully.")
    except ValueError:
        print("Please enter valid numeric values.")


def display_products(products):
    """Display all products."""
    print("\n===== INVENTORY =====")
    if not products:
        print("Inventory is empty.")
        return

    for name, details in products.items():
        value = details["price"] * details["quantity"]
        print(
            f"{name} | Price: {details['price']:.2f} | "
            f"Quantity: {details['quantity']} | Value: {value:.2f}"
        )


def search_product(products):
    """Search for a product by name."""
    name = input("Enter product name to search: ").strip()
    if name in products:
        details = products[name]
        print(f"Product: {name}")
        print(f"Price: {details['price']:.2f}")
        print(f"Quantity: {details['quantity']}")
    else:
        print("Product not found.")


def update_quantity(products):
    """Update the quantity of an existing product."""
    name = input("Enter product name: ").strip()
    if name not in products:
        print("Product not found.")
        return

    try:
        quantity = int(input("Enter new quantity: "))
        if quantity < 0:
            print("Quantity cannot be negative.")
            return
        products[name]["quantity"] = quantity
        print("Quantity updated successfully.")
    except ValueError:
        print("Please enter a whole number.")


def calculate_total_value(products):
    """Calculate the total value of all inventory."""
    total = 0
    for details in products.values():
        total += details["price"] * details["quantity"]
    print(f"Total inventory value: {total:.2f}")


def main():
    """Run the inventory application."""
    products = {}

    while True:
        print("\n===== INVENTORY MANAGEMENT =====")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Search Product")
        print("4. Update Quantity")
        print("5. Total Inventory Value")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_product(products)
        elif choice == "2":
            display_products(products)
        elif choice == "3":
            search_product(products)
        elif choice == "4":
            update_quantity(products)
        elif choice == "5":
            calculate_total_value(products)
        elif choice == "6":
            print("Exiting inventory system.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
