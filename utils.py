# utils.py
import json
from collections import defaultdict
import datetime

# Initialize packet counts and performance metrics
packet_counts = defaultdict(int)
performance_metrics = []

def log_packet_info(packet_info):
    """ Log packet info to a JSON file in a pretty format """
    with open('packet_logs.json', 'a') as f:
        json.dump(packet_info, f, indent=4)
        f.write(',\n')

def update_statistics(proto):
    """ Increment packet count for a protocol """
    packet_counts[proto] += 1

def log_performance(start_time, end_time):
    """ Log the packet processing time to a separate file """
    duration = end_time - start_time
    performance_metrics.append(duration.total_seconds())
    with open('performance_metrics.txt', 'a') as f:
        f.write(f"{datetime.datetime.now()} - Duration: {duration.total_seconds()} seconds\n")

def print_statistics():
    """ Print statistics of captured packets and performance metrics """
    print("\nPacket Counts:")
    for proto, count in packet_counts.items():
        print(f"{proto.upper()}: {count}")
    
    if performance_metrics:
        average_time = sum(performance_metrics) / len(performance_metrics)
        print(f"Average Processing Time: {average_time:.4f} seconds")

def format_packet(packet):
    """ Format packet information for logging """
    packet_info = {
        'timestamp': str(datetime.datetime.now()),
        'source_ip': packet[IP].src,
        'destination_ip': packet[IP].dst,
        'length': len(packet)
    }
    if TCP in packet:
        packet_info.update({
            'source_port': packet[TCP].sport,
            'destination_port': packet[TCP].dport,
            'protocol': 'TCP',
            'flags': packet[TCP].flags  # Include TCP flags in the packet info
        })
    elif UDP in packet:
        packet_info.update({
            'source_port': packet[UDP].sport,
            'destination_port': packet[UDP].dport,
            'protocol': 'UDP'
        })
    elif ICMP in packet:
        packet_info.update({
            'type': packet[ICMP].type,
            'code': packet[ICMP].code,
            'protocol': 'ICMP'
        })
    return packet_info
