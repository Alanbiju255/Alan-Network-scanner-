from scapy.all import ARP, Ether, srp
import socket
import os
import time

def print_banner():
    os.system("cls" if os.name == "nt" else "clear")
    banner = r"""
 _   _ ______ ______     _____  _____          _   _ 
| \ | || ___ \| ___ \   /  ___||  ___|        | \ | |
|  \| || |_/ /| |_/ /   \ `--. | |_ ___   ___ |  \| |
| . ` || ___ \|  __/     `--. \|  _/ _ \ / _ \| . ` |
| |\  || |_/ /| |___    /\__/ /| || (_) | (_) | |\  |
\_| \_/\____/ \____/    \____/ \_| \___/ \___/\_| \_/
                                                    
                   🔎 NET SCAN by Alan Biju
                   📱 Instagram: @alan.biju.75054
    -------------------------------------------------------------
    """
    print(banner)

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
    print("\n📡 Connected Devices:")
    print("IP Address\t\tMAC Address\t\t\tDevice Name")
    print("-" * 70)
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}\t{device['hostname']}")

if __name__ == "__main__":
    print_banner()
    ip_range = input("🌐 Enter IP range to scan (e.g., 192.168.1.0/24): ").strip()

    try:
        while True:
            print_banner()
            print(f"🔍 Scanning network: {ip_range}")
            devices = scan_network(ip_range)
            print_devices(devices)
            print("\n⏳ Waiting 10 seconds before next scan...\n")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n❌ Scan stopped by user. Exiting...")

