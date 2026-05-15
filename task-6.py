import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


stored_hash = hash_password("secret123")
print("Stored Hash:", stored_hash)


input_pwd = input("Enter password to login: ")
input_hash = hash_password(input_pwd)


if input_hash == stored_hash:
    print("Match Found! Access Granted.")
else:
    print("No Match! Access Denied.")
