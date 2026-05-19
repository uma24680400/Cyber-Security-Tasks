import secrets


def generate_otp():
    otp = "".join(secrets.choice("0123456789") for _ in range(6))
    print("OTP:", otp)


if __name__ == "__main__":
    generate_otp()
