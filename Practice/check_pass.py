import re
def check_password(password):
    if len(password)<8:
        return "Weak : Password should be at least 8 characters!"
    if not re.search("[a-z]",password):
        return "Weak : Password should have atleast one lowercase letter!"
    if not re.search("[A-Z]",password):
        return "Weak : Password should have atleast one uppercase letter!"
    if not re.search("[0-9]",password):
        return "Weak : password should have atleast one digit!"
    if not re.search("[!@#$%^&*Z(),.?/'':{}|<>]",password):
        return "Weak : password should contain atleast one special character!"
    return "Strong password!"

password = input("Enter password:")
print(check_password(password))