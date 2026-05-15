username_db = "admin"
password_db = "secure123"

user_input = input("Enter username: ")
pass_input = input("Enter password: ")

if user_input == username_db and pass_input == password_db:
    print("Login Successful! Welcome.")
else:
    print("Login Failed! Incorrect username or password.")
