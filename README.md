


# 🔍 Alan Network Scanner

🚀 A simple yet powerful Python tool to scan your local network and list connected devices using ARP requests.

---

## 👤 Author

- **Name:** Alan Biju  
- **Instagram:** [📷 @alan.biju.75054](https://instagram.com/alan.biju.75054)

---

## ✨ Features

✅ Discover devices on your local network  
✅ Shows **IP Address**, **MAC Address**, and **Hostname**  
✅ Scans run every **10 seconds** for real-time updates  
✅ Cross-platform support (Linux, macOS, Windows)  
✅ Lightweight & Easy to Use  

---

## 🧰 Requirements

- 🐍 Python 3.x
- 📦 [`scapy`](https://scapy.readthedocs.io/en/latest/)

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/alan-network-scanner.git
cd alan-network-scanner
````

2. Install dependencies:

```bash
pip install scapy
```

> 💡 **Note:** On Linux/macOS, run the script with `sudo` for full access to network scanning.

---

## ▶️ Usage

Run the scanner:

```bash
python scanner.py
```

🔢 When prompted, enter the IP range (e.g., `192.168.1.0/24`) to scan.

⏱️ The scanner will update every 10 seconds.

✋ Press `Ctrl + C` to stop scanning.

---

## 📸 Example Output

```
============================================================
             Alan Network Scanner
             Author : Alan Biju
             Instagram : alan.biju.75054
============================================================
Scanning network: 192.168.1.0/24

Connected Devices:
IP Address              MAC Address                      Device Name
----------------------------------------------------------------------
192.168.1.1             AA:BB:CC:DD:EE:FF                router.local
192.168.1.5             11:22:33:44:55:66                laptop.local

Waiting 10 seconds before next scan...
```

---

## ⚠️ Disclaimer

🚫 **For educational and ethical use only!**
Do **not** scan networks without explicit permission. Unauthorized scanning is illegal in many jurisdictions.

---

## 💬 Connect

Have suggestions or want to contribute? Open an issue or fork the repo! 😊

