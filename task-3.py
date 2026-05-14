import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8: strength += 1
    if re.search("[a-z]", password): strength += 1
    if re.search("[A-Z]", password): strength += 1
    if re.search("[0-9]", password): strength += 1
    if re.search("[!@#$%^&*]", password): strength += 1
    
    if strength == 5:
        return "Very Strong Password!"
    elif strength >= 3:
        return "Medium Strength Password."
    else:
        return "Very Weak Password, please change!"

pwd = input("Enter password to check: ")
print(check_password_strength(pwd))
