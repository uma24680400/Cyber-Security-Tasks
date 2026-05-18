import hashlib


def get_file_hash(path):
    hasher = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    h1 = get_file_hash("test_log.txt")
    print("Hash:", h1)
