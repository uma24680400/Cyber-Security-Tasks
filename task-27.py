import itertools


def brute_force_simulation(target_password, characters):
    attempts = 0
    for length in range(1, len(target_password) + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_str = "".join(guess)
            if guess_str == target_password:
                print("Password cracked:", guess_str)
                print("Total attempts:", attempts)
                return
    print("Password not found in simulation.")


if __name__ == "__main__":
    brute_force_simulation("cab", ["a", "b", "c"])
