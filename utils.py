# utils.py
from collections import defaultdict
import datetime

# Packet count by protocol
packet_counts = defaultdict(int)

def log_packet_info(packet_info):
    """ Log packet info to console """
    print(f"Packet: {packet_info}")

def update_statistics(proto):
    """ Increment packet count for a protocol """
    packet_counts[proto] += 1

def print_statistics():
    """ Print statistics of captured packets """
    print("\nPacket Counts:")
    for proto, count in packet_counts.items():
        print(f"{proto.upper()}: {count}")
