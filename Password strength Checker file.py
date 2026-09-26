import re

def check_password(password):
    score = 0

    # Length
    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Number
    if re.search(r"[0-9]", password):
        score += 1

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1

    # Result
    if score <= 2:
        return "Weak Score 2"
    elif score <= 4:
        return "Medium Score 4"
    else:
        return "Strong "


password = input("Enter your password: ")

strength = check_password(password)

print("Password Strength:", strength)