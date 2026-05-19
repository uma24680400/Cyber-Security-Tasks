import socket
from concurrent.futures import ThreadPoolExecutor
import sys
from datetime import datetime


TARGET = "localhost"  
START_PORT = 1
END_PORT = 1024      
MAX_THREADS = 100    

def scan_port(target, port):
    """
    Attempts to connect to a specific port on the target IP.
    Returns the port number if open, or None if closed.
    """
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
           
            s.settimeout(1.0)
            
            
            result = s.connect_ex((target, port))
            
           
            if result == 0:
                return port
    except Exception:
        
        pass
    return None

def main():
    try:
        target_ip = socket.gethostbyname(TARGET)
    except socket.gaierror:
        print("Host {TARGET} could not be resolved. Exiting.")
        sys.exit()

    print("-" * 50)
    print(f"Scanning Target: {target_ip}")
    print(f"Time Started:   {str(datetime.now())}")
    print("-" * 50)

    ports_to_scan = range(START_PORT, END_PORT + 1)
    open_ports = []

    
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        
        results = executor.map(lambda p: scan_port(target_ip, p), ports_to_scan)
        
        for result in results:
            if result is not None:
                print(f" Port {result}: OPEN")
                open_ports.append(result)

    print("-" * 50)
    print(f"Scan complete. Found {len(open_ports)} open ports.")
    print("-" * 50)

if __name__ == "__main__":
    main()
