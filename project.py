

import os
import socket

def ping_scanner():
    host = input("Enter IP Address or Website to Ping: ")

    print("\nScanning...\n")

    # For Windows
    response = os.system(f"ping -n 1 {host}")

    if response == 0:
        print(f"{host} is ONLINE")
    else:
        print(f"{host} is OFFLINE")



def port_checker():
    host = input("Enter Website or IP: ")
    port = int(input("Enter Port Number: "))

    print("\nChecking Port...\n")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} is OPEN on {host}")
    else:
        print(f"Port {port} is CLOSED on {host}")

    s.close()



def dns_lookup():
    domain = input("Enter Domain Name: ")

    try:
        ip = socket.gethostbyname(domain)
        print(f"\nIP Address of {domain} is: {ip}")

    except socket.gaierror:
        print("Invalid Domain Name")



while True:

    print("\n=================================")
    print("     CYBER NETWORK DETECTIVE")
    print("=================================")

    print("1. Ping Scanner")
    print("2. Port Checker")
    print("3. DNS Lookup Tool")
    print("4. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == '1':
        ping_scanner()

    elif choice == '2':
        port_checker()

    elif choice == '3':
        dns_lookup()

    elif choice == '4':
        print("\nExiting Program...")
        break

    else:
        print("\nInvalid Choice! Try Again.")
