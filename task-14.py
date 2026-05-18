import hashlib
import os


def find_dups(target):
    hashes = {}
    for root, dirs, files in os.walk(target):
        for file in files:
            p = os.path.join(root, file)
            h = hashlib.md5()
            try:
                with open(p, "rb") as f:
                    for c in iter(lambda: f.read(4096), b""):
                        h.update(c)
                f_hash = h.hexdigest()
                if f_hash in hashes:
                    print("Duplicate:", p, "Original:", hashes[f_hash])
                else:
                    hashes[f_hash] = p
            except:
                continue


if __name__ == "__main__":
    find_dups(".")
