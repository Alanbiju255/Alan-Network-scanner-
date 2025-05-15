

# Alan Network Scanner

A simple Python-based network scanner that identifies all devices connected to your Wi-Fi network. It shows the IP address, MAC address, and device name (if available) of each connected device.

---

## Features

- Scans your local network using ARP
- Displays:
  - IP Address
  - MAC Address
  - Device Name (Hostname)
- Simple command-line interface
- Author banner on startup

---

## Banner

============================================================ Alan Network Scanner Author : Alan Biju Instagram : alan.biju.75054

---

## Usage

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/alan-network-scanner.git
cd alan-network-scanner

2. Install dependencies:

pip install scapy

3. Run the scanner:

Linux/Mac:

sudo python3 alan_scanner.py

Windows:

python alan_scanner.py


---

Example Output

Enter IP range (e.g., 192.168.1.1/24): 192.168.1.1/24

Connected Devices:
IP Address          MAC Address              Device Name
----------------------------------------------------------------------
192.168.1.1         58:ef:68:23:4a:aa        my-router.local
192.168.1.5         44:6d:57:1f:2e:cc        AlanPhone
192.168.1.10        00:1A:2B:3C:4D:5E        Unknown


---

Notes

Run the script as root/administrator to allow ARP scanning.

This tool only works on local networks (LAN/Wi-Fi).

Hostnames may show as "Unknown" if not discoverable via reverse DNS.



---

Author

Alan Biju
Instagram: @alan.biju.75054


---

---
