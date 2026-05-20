import logging


logger = logging.getLogger("NetworkLogger")
logger.setLevel(logging.INFO)


file_handler = logging.FileHandler("network_traffic.log")
formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def log_network_event(event_type, source_ip, dest_ip, status):
    message = f"Type: {event_type} | Src: {source_ip} -> Dst: {dest_ip} | Status: {status}"
    logger.info(message)
    print(f"[Logged] {message}")

if __name__ == "__main__":
    print("[+] Initializing Network Logging Simulator...")
    log_network_event("CONNECTION_ESTABLISHED", "192.168.1.50", "10.0.0.1", "SUCCESS")
    log_network_event("DATA_TRANSFER", "192.168.1.50", "10.0.0.1", "200 OK")
    log_network_event("DISCONNECT", "192.168.1.50", "10.0.0.1", "CLOSED")
