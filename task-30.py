def detect_weak_passwords(accounts, common_passwords):
    for user, pwd in accounts.items():
        if len(pwd) < 8:
            print("Weak:", user, "(Too short)")
        elif pwd.lower() in common_passwords:
            print("Weak:", user, "(Commonly used password)")
        elif pwd.isdigit() or pwd.isalpha():
            print("Weak:", user, "(Needs mixed characters)")
        else:
            print("Secure:", user)


if __name__ == "__main__":
    users = {
        "user1": "12345",
        "user2": "password",
        "user3": "qwerty",
        "user4": "Tr0ub4d&r",
    }
    common = ["password", "123456", "qwerty", "admin"]
    detect_weak_passwords(users, common)
