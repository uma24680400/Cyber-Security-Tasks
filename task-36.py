from scapy.all import sniff, IP

def process_packet(packet):
   
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        print(f"[+] Packet: {src_ip} -> {dst_ip} | Protocol: {proto}")

if __name__ == "__main__":
    print("[+] Starting educational packet sniffer... (Press Ctrl+C to stop)")
    print("[!] Ensure you are running this terminal as Administrator/Root.")
    
   
    sniff(prn=process_packet, count=10)
