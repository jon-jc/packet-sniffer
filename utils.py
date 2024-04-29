# utils.py
import json
from collections import defaultdict
import datetime

# Initialize packet counts and performance metrics
packet_counts = defaultdict(int)
performance_metrics = []

def log_packet_info(packet_info):
    """ Log packet info to a JSON file """
    with open('packet_logs.json', 'a') as f:
        json.dump(packet_info, f)
        f.write('\n')

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
