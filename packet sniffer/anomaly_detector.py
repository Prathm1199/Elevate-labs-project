import time
from alert_system import log_alert

packet_counts = {}  # {src_ip: [timestamps]}

PORT_SCAN_THRESHOLD = 10  # ports per 10 seconds
FLOOD_THRESHOLD = 50  # packets per 10 seconds


def detect_anomaly(packet_info):
    timestamp, src_ip, dst_ip, src_port, dst_port, proto = packet_info

    # Initialize tracking
    if src_ip not in packet_counts:
        packet_counts[src_ip] = []

    packet_counts[src_ip].append((timestamp, dst_port))

    # Remove timestamps older than 10 seconds
    packet_counts[src_ip] = [(t, p) for t, p in packet_counts[src_ip] if timestamp - t < 10]

    # Flood detection
    if len(packet_counts[src_ip]) > FLOOD_THRESHOLD:
        log_alert(f"Flooding detected from {src_ip} ({len(packet_counts[src_ip])} packets in 10s)")

    # Port scanning detection
    ports = {p for t, p in packet_counts[src_ip]}
    if len(ports) > PORT_SCAN_THRESHOLD:
        log_alert(f"Port scanning detected from {src_ip} ({len(ports)} unique ports in 10s)")
