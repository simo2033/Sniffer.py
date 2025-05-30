from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def packet_callback(packet):
    timestamp = datetime.now().strftime("%H:%M:%S")

    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = "OTHER"

        if packet.haslayer(TCP):
            proto = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif packet.haslayer(UDP):
            proto = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        elif packet.haslayer(ICMP):
            proto = "ICMP"
            sport = "-"
            dport = "-"

        print(f"[{timestamp}] {proto} {ip_src}:{sport} -> {ip_dst}:{dport}")
    else:
        print(f"[{timestamp}] Non-IP packet captured")

def main():
    print("Avvio dello sniffer (CTRL+C per interrompere)...\n")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
