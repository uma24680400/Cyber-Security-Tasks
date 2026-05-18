def detect_login_attempts(log_path):
    failed = 0
    success = 0
    try:
        with open(log_path, "r") as file:
            for line in file:
                if "failed" in line.lower():
                    print("ALERT Failed login:", line.strip())
                    failed += 1
                elif "success" in line.lower():
                    success += 1
        print("Success:", success)
        print("Failed:", failed)
    except FileNotFoundError:
        print("Error")


if __name__ == "__main__":
    detect_login_attempts("test_log.txt")
