import re

def password_strength(password):
    if len(password) < 8:
        print("Password is too short")
        return

    if not re.search(r"[A-Z]", password):
        print("Password should have at least one uppercase letter")
        return

    if not re.search(r"[a-z]", password):
        print("Password should have at least one lowercase letter")
        return

    if not re.search(r"[0-9]", password):
        print("Password should have at least one digit")
        return

    if not re.search(r"[!@#$%^&*(),./<>?]", password):
        print("Password should have at least one special character")
        return

    print("Password is strong")

user_password = input("Enter a password to check its strength: ")
password_strength(user_password)