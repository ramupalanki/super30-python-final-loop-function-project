"""Mini Authentication System."""

def login(username, password, stored_username, stored_password):
    """Check whether supplied credentials are correct."""
    return username == stored_username and password == stored_password


def logout():
    """Display logout confirmation."""
    print("You have been logged out successfully.")


def main():
    """Run the authentication system."""
    stored_username = "student"
    stored_password = "Python@123"
    max_attempts = 3
    attempts = 0
    logged_in = False

    print("===== MINI AUTHENTICATION SYSTEM =====")

    while attempts < max_attempts:
        username = input("Enter username: ").strip()
        password = input("Enter password: ")

        if login(username, password, stored_username, stored_password):
            print("Login successful!")
            logged_in = True
            break

        attempts += 1
        remaining = max_attempts - attempts
        print("Login failed.")
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")

    if not logged_in:
        print("Maximum login attempts reached. Access denied.")
        return

    while logged_in:
        print("\n1. Logout")
        print("2. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            logout()
            logged_in = False
        elif choice == "2":
            print("Exiting application.")
            logged_in = False
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
