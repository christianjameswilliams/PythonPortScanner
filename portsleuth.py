import sys 
import socket
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

#Prompt user for target IP and store it as a string
targetIP = str(input("Target IP: "))
#Prompt user for port scan type, store it as a string, and convert to uppercase
targetPort = str(input("Port scan type: ")).upper()

if targetPort == "A":
	portRange = range(1, 65535)
elif targetPort == "W":
	portRange = [20, 21, 22, 23, 25, 53, 69, 80, 110, 123, 135, 143, 443, 445, 3389]
elif targetPort == "C":
	customPorts = str(input("Specific ports (comma-separated): "))
	#Split user input by commas, remove extra spaces, and save as list
	portRange = [int(port.strip()) for port in customPorts.split(',')]
else:
	print("Invalid input. Exiting...")
	sys.exit()

#Banner to separate output
print("_" * 50)
print("Scan Target: " + targetIP)
print("Scanning Ports: " + str(portRange))
print("Scan start: " + str(datetime.now()))
print("_" * 50)

try:
    #Iterates over list of ports
	for port in portRange:
		#Creates a new socket using IPv4 (AF_INET) and TCP (SOCK_STREAM)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5)
		
        #Attempt to connect to target IP and port
		result = s.connect_ex((targetIP,port))
		if result == 0:
			print("[*] Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\n Exiting :(")
	sys.exit()
	
except socket.error:
	print("\ Host not responding :(")
	sys.exit()