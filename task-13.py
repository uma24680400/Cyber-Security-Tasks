import os


def scan_dir(target):
    for root, dirs, files in os.walk(target):
        for file in files:
            p = os.path.join(root, file)
            print(p, os.path.getsize(p))


if __name__ == "__main__":
    scan_dir(".")
