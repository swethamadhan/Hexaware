def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    elif not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    elif not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit."
    else:
        return True, "Password is valid."

def main():
    password = input("Create a password for your bank account: ")

    is_valid, message = validate_password(password)

    if is_valid:
        print(message)
    else:
        print("Invalid password:", message)

if __name__ == "__main__":
    main()
