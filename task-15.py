def caesar_encrypt(text, shift):
    res = ""
    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            res += chr((ord(char) - start + shift) % 26 + start)
        else:
            res += char
    return res


if __name__ == "__main__":
    print(caesar_encrypt("SecretMessage123", 4))
