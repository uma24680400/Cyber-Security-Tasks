import socket


def get_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2.0)
        s.connect((ip, port))
        s.send(b"WhoAreYou\r\n")
        banner = s.recv(1024)
        print("Port", port, "Banner:", banner.decode().strip())
    except:
        print("Port", port, "No response")
    finally:
        s.close()


if __name__ == "__main__":
    get_banner("127.0.0.1", 22)
