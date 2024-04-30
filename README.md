# Packet Sniffer

Welcome to the Packet Sniffer project! This tool allows you to capture and analyze network packets, providing insights into network traffic and performance.

## Overview
Packet sniffing is a technique used to intercept and log traffic passing over a network. This project aims to provide a simple yet powerful packet sniffer tool implemented in Python.

## Features
- **Packet Capture**: Capture network packets in real-time.
- **Protocol Filtering**: Select specific protocols for capturing.
- **Detailed Packet Logging**: Log comprehensive packet information for analysis.
- **Performance Metrics**: Track packet processing times for performance analysis.
- **User-Friendly Interface**: Intuitive command-line interface for easy operation.

## Installation
1. Clone the repository:
```sh
git clone https://github.com/your_username/packet-sniffer.git
```


2. Install dependencies:
  ```sh
pip install scapy
```

## Usage
1. Navigate to the project directory:

```sh
cd packet-sniffer
```

2. Run the packet sniffer:
```sh
python main.py
```

3. Follow the prompts to select protocols and start capturing packets:
 ```sh
## Packet Logging
The packet sniffer logs captured packet details to a JSON file (`packet_logs.json`) in the source directory. Each packet is logged in the following format:

```json
{
    "src": "10.0.0.31",
    "dst": "20.50.201.200",
    "length": 54,
    "protocol": "tcp"
}

   ```
