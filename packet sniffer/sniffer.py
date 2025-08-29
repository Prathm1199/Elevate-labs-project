from scapy.all import sniff, IP, TCP, UDP
import time
from database import log_packet, get_summary
from anomaly_detector import detect_anomaly


def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        src_port = packet[TCP].sport if TCP in packet else (packet[UDP].sport if UDP in packet else 0)
        dst_port = packet[TCP].dport if TCP in packet else (packet[UDP].dport if UDP in packet else 0)
        length = len(packet)
        flags = packet[TCP].flags if TCP in packet else None

        packet_info = (time.time(), src_ip, dst_ip, src_port, dst_port, proto)

        # Log packet to database
        log_packet(packet_info)

        # Check for anomalies
        detect_anomaly(packet_info)

        # Print packet summary in CLI
        print(f"{src_ip}:{src_port} -> {dst_ip}:{dst_port} | proto={proto} | len={length} | flags={flags}")


def main():
    print("Starting packet sniffer...")
    sniff(prn=packet_callback, store=False)


if __name__ == "__main__":
    main()
