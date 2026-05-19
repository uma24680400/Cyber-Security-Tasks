import socket


def whois_lookup(domain):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.iana.org", 43))
        s.send((domain + "\r\n").encode())
        res = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            res += data
        print(res.decode())
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    whois_lookup("google.com")
