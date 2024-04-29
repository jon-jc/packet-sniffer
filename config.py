# config.py

# Supported protocols as recognized by Scapy filters
SUPPORTED_PROTOCOLS = ['tcp', 'udp', 'icmp']

# User selected protocols for sniffing
selected_protocols = []

def set_protocols(protocols):
    global selected_protocols
    selected_protocols = protocols

def get_protocols():
    return selected_protocols
