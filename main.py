from config import SUPPORTED_PROTOCOLS, set_protocols
from sniffer import start_sniffing
from utils import print_statistics

def get_user_protocol_choice():
    """ Prompt the user to choose protocols to sniff and validate the input. """
    while True:
        print("\nAvailable Protocols to Sniff: " + ', '.join([p.upper() for p in SUPPORTED_PROTOCOLS]))
        protocols_input = input("Enter protocols to sniff (comma-separated, e.g., TCP, UDP): ").strip().lower()
        
        # Validate input
        selected_protocols = [proto.strip() for proto in protocols_input.split(',') if proto.strip() in SUPPORTED_PROTOCOLS]
        
        if selected_protocols:
            return selected_protocols
        else:
            print("Invalid input. Please enter valid protocols from the list above.")

def main():
    print("Welcome to the Packet Sniffer")
    selected_protocols = get_user_protocol_choice()
    
    # Set the selected protocols for sniffing
    set_protocols(selected_protocols)

    try:
        print("\nStarting to sniff. Press CTRL+C to stop.")
        start_sniffing()
    except KeyboardInterrupt:
        print("\nSniffing stopped by user.")
        print_statistics()

if __name__ == "__main__":
    main()