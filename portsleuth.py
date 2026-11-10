import sys
import socket
import ipaddress
from datetime import datetime

print("░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░▒▓████████▓▒░       ░▒▓███████▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░")
print("░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░")
print("░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  ░▒▓█▓▒░           ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓████████▓▒░")
print(" ▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                 ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░")
print("░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░                 ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░")
print("░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░          ░▒▓███████▓▒░░▒▓████████▓▒░▒▓████████▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░   ░▒▓█▓▒░░▒▓█▓▒░")
print("\n")
print("Port scan options: (A)ll, (W)ell known, (C)ustom")
print("\n")


def parse_custom_ports(value):
    """Return unique, valid TCP ports in the order provided."""
    entries = value.split(",")
    if not value.strip() or any(not entry.strip() for entry in entries):
        raise ValueError("Enter one or more comma-separated ports (1-65535).")

    ports = []
    seen = set()
    for entry in entries:
        text = entry.strip()
        if not text.isascii() or not text.isdecimal():
            raise ValueError(f"Invalid port '{text}': use whole numbers from 1 to 65535.")
        port = int(text)
        if not 1 <= port <= 65535:
            raise ValueError(f"Port {port} is outside the valid range (1-65535).")
        if port not in seen:
            ports.append(port)
            seen.add(port)
    return ports


try:
    targetIP = input("Target IP: ").strip()
    try:
        targetIP = str(ipaddress.IPv4Address(targetIP))
    except ipaddress.AddressValueError:
        raise ValueError("Enter a valid IPv4 address (for example, 192.168.1.1).")

    targetPort = input("Port scan type: ").strip().upper()
    if targetPort == "A":
        portRange = range(1, 65536)
    elif targetPort == "W":
        portRange = [20, 21, 22, 23, 25, 53, 69, 80, 110, 123, 135, 143, 443, 445, 3389]
    elif targetPort == "C":
        portRange = parse_custom_ports(input("Specific ports (comma-separated): "))
    else:
        raise ValueError("Invalid scan type. Choose A, W, or C.")
except ValueError as error:
    print(f"Input error: {error}")
    sys.exit(1)
except (EOFError, KeyboardInterrupt):
    print("\nInput canceled. Exiting...")
    sys.exit(1)

# Banner to separate output
print("_" * 50)
print("Scan Target: " + targetIP)
print("Scanning Ports: " + str(portRange))
print("Scan start: " + str(datetime.now()))
print("_" * 50)

try:
    # Iterates over list of ports
    for port in portRange:
        # Creates a new socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        # Attempt to connect to target IP and port
        result = s.connect_ex((targetIP, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting :(")
    sys.exit()

except socket.error:
    print("\ Host not responding :(")
    sys.exit()
#test write
