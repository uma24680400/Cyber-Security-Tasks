import socket


def find_subdomains(domain, subs):
    for sub in subs:
        target = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(target)
            print("Found:", target, "->", ip)
        except socket.gaierror:
            continue


if __name__ == "__main__":
    sub_list = ["www", "mail", "ftp", "blog", "admin"]
    find_subdomains("google.com", sub_list)
