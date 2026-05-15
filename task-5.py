import hashlib

def hash_password(password):
    
    password_bytes = password.encode()
    hash_obj = hashlib.sha256(password_bytes)
    return hash_obj.hexdigest()

my_pwd = input("Enter password to hash: ")
hashed = hash_password(my_pwd)
print("SHA256 Hash:", hashed)
