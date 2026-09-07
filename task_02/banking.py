"""Menu-driven Banking Application."""

def check_balance(balance):
    """Display the current account balance."""
    print(f"Current balance: {balance:.2f}")


def deposit(balance, history):
    """Deposit money and record the transaction."""
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return balance
        balance += amount
        history.append(f"Deposited {amount:.2f}")
        print(f"Deposit successful. New balance: {balance:.2f}")
    except ValueError:
        print("Please enter a valid amount.")
    return balance


def withdraw(balance, history):
    """Withdraw money if sufficient balance is available."""
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            history.append(f"Withdrew {amount:.2f}")
            print(f"Withdrawal successful. New balance: {balance:.2f}")
    except ValueError:
        print("Please enter a valid amount.")
    return balance


def show_history(history):
    """Display all transactions."""
    print("\n===== TRANSACTION HISTORY =====")
    if not history:
        print("No transactions yet.")
        return
    for number, transaction in enumerate(history, start=1):
        print(f"{number}. {transaction}")


def main():
    """Run the banking application."""
    balance = 0.0
    history = []

    while True:
        print("\n===== BANKING APPLICATION =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance, history)
        elif choice == "3":
            balance = withdraw(balance, history)
        elif choice == "4":
            show_history(history)
        elif choice == "5":
            print("Thank you for using the banking application.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
