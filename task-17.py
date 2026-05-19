def xor_cipher(text, key):
    return "".join(chr(ord(c) ^ ord(key)) for c in text)


if __name__ == "__main__":
    orig = "Confidential"
    enc = xor_cipher(orig, "K")
    dec = xor_cipher(enc, "K")
    print("Encrypted:", repr(enc))
    print("Decrypted:", dec)
