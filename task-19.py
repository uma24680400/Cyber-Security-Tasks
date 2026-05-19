import os
from hashlib import pbkdf2_hmac


def store_cred(password):
    salt = os.urandom(16)
    key = pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    print("Salt:", salt.hex())
    print("Key:", key.hex())


if __name__ == "__main__":
    store_cred("UserPassword123")
