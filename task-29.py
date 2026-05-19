import hashlib


def crack_password(target_hash, wordlist):
    for word in wordlist:
        guess_hash = hashlib.sha256(word.encode()).hexdigest()
        if guess_hash == target_hash:
            print("Password found:", word)
            return
    print("Password not in wordlist")


if __name__ == "__main__":
    target = "5e88427e72a6683914439908466762e33f500a24e4f0a4a2d83197299e04c723"
    passwords = ["admin", "123456", "password", "secret"]
    crack_password(target, passwords)
