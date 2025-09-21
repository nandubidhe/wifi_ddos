WiFi Deauthentication Attack Tool
This tool performs a WiFi deauthentication attack against a target network. It sends deauthentication packets to disconnect clients from the target network.

Features
Sends deauthentication packets to both clients and access points
Supports monitor mode interfaces
Can specify target network channel
Configurable attack duration
Displays real-time packet statistics


Requirements
Python 3.x
Scapy library
Wireless adapter capable of monitor mode


Installation
git clone https://github.com/nandubidhe/wifi-ddos.git
cd wifi-ddos
python wifi_ddos.py install


Usage
python wifi_ddos.py -i <interface> -g <gateway_mac> --bssid <target_bssid>


Arguments
-i, --interface: Interface to use (must be in monitor mode)
-g, --gateway: Gateway MAC address
--bssid: Target network BSSID
--channel: Target network channel (optional)
--duration: Attack duration in seconds (default: 60)


Example
python wifi_ddos.py -i wlan0 -g AA:BB:CC:DD:EE:FF --bssid 11:22:33:44:55:66 --channel 6



Notes
This tool requires root privileges to put the wireless interface in monitor mode.
The target network must be within range of the wireless adapter.
Use responsibly and only on networks you have permission to test.



License
This project is licensed under the MIT License. See the LICENSE file for details.

