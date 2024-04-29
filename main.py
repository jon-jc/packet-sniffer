from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        print(f"From {src_ip}:{src_port} to {dst_ip}:{dst_port}")

def main():
    sniff(filter="tcp", prn=packet_callback, store=False)

if __name__ == "__main__":
    main()