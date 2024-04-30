# sniffer.py
from scapy.all import sniff, IP, TCP
from config import get_protocols
from utils import log_packet_info, update_statistics

def packet_callback(packet):
    """ Callback to process each captured packet """
    if IP in packet and TCP in packet:
        ip_layer = packet[IP]
        tcp_layer = packet[TCP]

        # Check if the protocol is selected for sniffing
        if 'tcp' in get_protocols():
            packet_info = {
                'src': ip_layer.src,
                'dst': ip_layer.dst,
                'length': len(packet),
                'protocol': 'tcp',
                'flags': {
                    'SYN': bool(tcp_layer.flags & 0x02),
                    'ACK': bool(tcp_layer.flags & 0x10),
                    'FIN': bool(tcp_layer.flags & 0x01),
                    'RST': bool(tcp_layer.flags & 0x04),
                    # Add more flags as needed
                }
            }
            log_packet_info(packet_info)
            update_statistics('tcp')

def start_sniffing():
    """ Start sniffing packets """
    protocols = " or ".join(get_protocols())
    sniff(filter=protocols, prn=packet_callback, store=False)
