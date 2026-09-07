"""Super30 Python Utility Application."""

def calculator():
    """Perform a basic arithmetic calculation."""
    try:
        first = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        second = float(input("Enter second number: "))

        if operator == "+":
            result = first + second
        elif operator == "-":
            result = first - second
        elif operator == "*":
            result = first * second
        elif operator == "/":
            if second == 0:
                print("Cannot divide by zero.")
                return
            result = first / second
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")


    except ValueError:
        print("Please enter valid numbers.")


def palindrome_checker():
    """Check whether a string is a palindrome."""
    text = input("Enter text: ").strip().lower().replace(" ", "")
    if text == text[::-1]:
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


def is_prime(number):
    """Return True if the number is prime."""
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def prime_checker():
    """Check whether a number is prime."""
    try:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(f"{number} is prime.")
        else:
            print(f"{number} is not prime.")
    except ValueError:
        print("Please enter a whole number.")


def factorial_calculator():
    """Calculate a factorial using a loop."""
    try:
        number = int(input("Enter a non-negative integer: "))
        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        factorial = 1
        for value in range(1, number + 1):
            factorial *= value
        print(f"{number}! = {factorial}")
    except ValueError:
        print("Please enter a whole number.")


def multiplication_table():
    """Display a multiplication table."""
    try:
        number = int(input("Enter a number: "))
        for multiplier in range(1, 11):
            print(f"{number} x {multiplier} = {number * multiplier}")
    except ValueError:
        print("Please enter a whole number.")


def number_analyzer():
    """Analyze a single number."""
    try:
        number = int(input("Enter a number: "))
        if number > 0:
            sign = "Positive"
        elif number < 0:
            sign = "Negative"
        else:
            sign = "Zero"

        if number % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"

        print(f"Sign: {sign}")
        print(f"Parity: {parity}")
    except ValueError:
        print("Please enter a whole number.")


def password_checker():
    """Check basic password strength."""
    password = input("Enter password: ")
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("Strong password.")
    else:
        print("Password needs 8+ characters, uppercase, lowercase, number, and special character.")


def main():
    """Run the utility menu until Exit is selected."""
    while True:
        print("\n===== SUPER30 PYTHON UTILITY APPLICATION =====")
        print("1. Calculator")
        print("2. Palindrome Checker")
        print("3. Prime Checker")
        print("4. Factorial Calculator")
        print("5. Multiplication Table")
        print("6. Number Analyzer")
        print("7. Password Checker")
        print("8. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            palindrome_checker()
        elif choice == "3":
            prime_checker()
        elif choice == "4":
            factorial_calculator()
        elif choice == "5":
            multiplication_table()
        elif choice == "6":
            number_analyzer()
        elif choice == "7":
            password_checker()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
