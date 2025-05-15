

from scapy.all import ARP, Ether, srp
import socket
import os

def print_banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 60)
    print("             Alan Network Scanner")
    print("             Author : Alan Biju")
    print("             Instagram : alan.biju.75054")
    print("=" * 60)

def scan_network(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        devices.append({
            "ip": ip,
            "mac": mac,
            "hostname": hostname
        })

    return devices

def print_devices(devices):
    print("\nConnected Devices:")
    print("IP Address\t\tMAC Address\t\t\tDevice Name")
    print("-" * 70)
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}\t{device['hostname']}")

if __name__ == "__main__":
    print_banner()
    ip_range = input("Enter IP range (e.g., 192.168.1.1/24): ")
    devices = scan_network(ip_range)
    print_devices(devices)
