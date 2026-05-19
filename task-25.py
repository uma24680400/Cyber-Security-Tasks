import socket


def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(domain, "IP:", ip)
    except:
        print("Could not resolve domain")


if __name__ == "__main__":
    dns_lookup("google.com")
