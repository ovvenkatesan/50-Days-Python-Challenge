# SimplePassword.py

def check_password_strength(password, min_length=8):
    """
    Checks if a password meets the minimum length requirement.

    Args:
        password (str): The password string to check.
        min_length (int): The minimum required length for the password.

    Returns:
        bool: True if the password meets the minimum length, False otherwise.
    """
    if len(password) >= min_length:
        return True
    else:
        return False

def main():
    print("Simple Password Strength Checker")
    print("--------------------------------")

    minimum_required_length = 8 # You can change this value

    while True:
        user_password = input(f"Enter a password (minimum {minimum_required_length} characters): ")

        if check_password_strength(user_password, minimum_required_length):
            print("Password meets the minimum length requirement. Good job!")
            break # Exit loop if password is valid
        else:
            print(f"Password is too short. It must be at least {minimum_required_length} characters long.")
            print("Please try again.")
        print("-" * 30) # Separator for clarity

    print("\nPassword check complete.")

if __name__ == "__main__":
    main()
