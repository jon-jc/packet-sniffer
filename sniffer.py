# sniffer.py
from scapy.all import sniff, IP
from config import get_protocols
from utils import log_packet_info, update_statistics

def packet_callback(packet):
    """ Callback to process each captured packet """
    if IP in packet:
        ip_layer = packet[IP]
        if ip_layer.proto in [6, 17, 1]:  # TCP=6, UDP=17, ICMP=1
            proto_name = {6: 'tcp', 17: 'udp', 1: 'icmp'}.get(ip_layer.proto, 'unknown')
            if proto_name in get_protocols():
                packet_info = {
                    'src': ip_layer.src,
                    'dst': ip_layer.dst,
                    'length': len(packet),
                    'protocol': proto_name
                }
                log_packet_info(packet_info)
                update_statistics(proto_name)

def start_sniffing():
    """ Start sniffing packets """
    protocols = " or ".join(get_protocols())
    sniff(filter=protocols, prn=packet_callback, store=False)
