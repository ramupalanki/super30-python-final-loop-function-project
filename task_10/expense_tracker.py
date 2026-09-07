"""Expense Tracker Application."""

def add_expense(expenses):
    """Add an expense to the tracker."""
    name = input("Enter expense name: ").strip()
    if not name:
        print("Expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        expenses.append({"name": name, "amount": amount})
        print("Expense added successfully.")
    except ValueError:
        print("Please enter a valid amount.")


def view_expenses(expenses):
    """Display all recorded expenses."""
    print("\n===== EXPENSES =====")
    if not expenses:
        print("No expenses recorded.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['name']} - {expense['amount']:.2f}")


def calculate_total(expenses):
    """Calculate the total of all expenses."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total expenses: {total:.2f}")
    return total


def find_highest_expense(expenses):
    """Find and display the highest expense."""
    if not expenses:
        print("No expenses recorded.")
        return

    highest = expenses[0]
    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print(f"Highest expense: {highest['name']} - {highest['amount']:.2f}")


def main():
    """Run the expense tracker."""
    expenses = []

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Find Highest Expense")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            find_highest_expense(expenses)
        elif choice == "5":
            print("Exiting expense tracker.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
