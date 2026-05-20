import socket


VULNERABILITY_DATABASE = {
    "VSFTPD 2.3.4": "CVE-2011-2523 - Backdoor Command Execution (High Risk)",
    "OpenSSH 7.2p2": "CVE-2016-6210 - User Enumeration Vulnerability (Medium Risk)",
    "Apache 2.4.41": "CVE-2020-1927 - URL Redirection Vulnerability (Low Risk)"
}

def grab_banner(target_ip, target_port):
    """Connects to a host and returns its service banner."""
    try:
        
        socket.setdefaulttimeout(3)
        s = socket.socket()
        
        print(f"[*] Connecting to {target_ip}:{target_port}...")
        s.connect((target_ip, target_port))
        
        
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        return banner
    except Exception as e:
        return None
    finally:
        s.close()

def scan_target(target_ip, target_port):
    """Grabs the banner and checks it against the vulnerability database."""
    banner = grab_banner(target_ip, target_port)
    
    if not banner:
        print(f"[-] Could not retrieve banner from {target_ip}:{target_port} (Port may be closed or silent).")
        return

    print(f"[+] Service Banner Retreived: '{banner}'")
    
   
    found_vuln = False
    for service_version, vulnerability in VULNERABILITY_DATABASE.items():
        if service_version.lower() in banner.lower():
            print(f"🚨 [VULNERABILITY FOUND] Match discovered!")
            print(f"   -> Details: {vulnerability}")
            found_vuln = True
            
    if not found_vuln:
        print("[✓] No known vulnerabilities found in the banner string.")

if __name__ == "__main__":
    print("[+] Launching Educational Vulnerability Scanner...")
    
   
    scan_target("127.0.0.1", 21) 
    
    print("\n--- Simulation Test ---")
   
    simulated_banner = "Welcome to vsFTPd 2.3.4 server"
    print(f"Simulating detection for: '{simulated_banner}'")
    for service_version, vulnerability in VULNERABILITY_DATABASE.items():
        if service_version.lower() in simulated_banner.lower():
            print(f"🚨 [VULNERABILITY FOUND] Match discovered!")
            print(f"   -> Details: {vulnerability}")
