"""Password Strength Checker."""

def check_password_strength(password):
    """Check required password characteristics and return a result."""
    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_number = True
        else:
            has_special = True

    if len(password) < 8:
        return "Weak: password must contain at least 8 characters."
    if not has_uppercase:
        return "Weak: add at least one uppercase letter."
    if not has_lowercase:
        return "Weak: add at least one lowercase letter."
    if not has_number:
        return "Weak: add at least one number."
    if not has_special:
        return "Weak: add at least one special character."

    return "Strong password!"


def main():
    """Run the password strength checker."""
    print("===== PASSWORD STRENGTH CHECKER =====")
    password = input("Enter password: ")
    print(check_password_strength(password))


if __name__ == "__main__":
    main()
