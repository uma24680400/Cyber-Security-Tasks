
FIREWALL_RULES = [
    ("ALLOW", "192.168.1.10", 80),
    ("ALLOW", "192.168.1.20", 443),
    ("BLOCK", "10.0.0.5", 22),
    ("BLOCK", "*", 3389)  
]

def filter_packet(src_ip, dest_port):
    for action, rule_ip, rule_port in FIREWALL_RULES:
        if (rule_ip == "*" or rule_ip == src_ip) and rule_port == dest_port:
            return action
    return "BLOCK" 

if __name__ == "__main__":
    print("[+] Initializing Firewall Rule Engine...")
    
    traffic_tests = [
        ("192.168.1.10", 80),
        ("10.0.0.5", 22),
        ("192.168.1.55", 3389),
        ("192.168.1.20", 443)
    ]
    
    for ip, port in traffic_tests:
        action = filter_packet(ip, port)
        status = "✓ PASSED" if action == "ALLOW" else "🚨 BLOCKED"
        print(f"Packet [{ip}:{port}] -> {status}")
