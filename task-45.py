import socket
from datetime import datetime


COMMON_SERVICES = {
    21: "FTP (File Transfer Protocol)",
    22: "SSH (Secure Shell)",
    23: "Telnet",
    25: "SMTP (Simple Mail Transfer Protocol)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Hypertext Transfer Protocol)",
    110: "POP3 (Post Office Protocol)",
    443: "HTTPS (Secure HTTP)",
    3389: "RDP (Remote Desktop Protocol)"
}

def scan_services(target_host, ports_to_scan):
    try:
        
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"\n[-] DNS Resolution failed. Cannot resolve target: {target_host}")
        return

    print("-" * 50)
    print(f"Scanning Target : {target_host} ({target_ip})")
    print(f"Time Started    : {str(datetime.now())}")
    print("-" * 50)

    open_services_found = 0

    for port in ports_to_scan:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
        s.settimeout(1.0)
        
        
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            service_name = COMMON_SERVICES.get(port, "Unknown Service")
            print(f"[✓] Port {port:5} : OPEN   -> Service: {service_name}")
            open_services_found += 1
        s.close()

    print("-" * 50)
    print(f"[!] Scan Completed. Found {open_services_found} active network service(s).")

if __name__ == "__main__":
   
    target = "127.0.0.1"
    
    
    ports_list = sorted(list(COMMON_SERVICES.keys()))
    
    scan_services(target, ports_list)
