#!/bin/python3

import sys
import socket
from datetime import datetime

# Define our target

if len(sys.argv) == 2:  # argv is the amount of arguments we are giving; must have 2 arguments or it will break
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

# Add a pretty banner
print("-" * 50)
print("Scanning target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)
	
try:
	for port in range (50,85):  # 50,85 is the port range we are scanning
	
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #s is the variable; AF_INET is IPv4 address, socklet is port
		
		socket.setdefaulttimeout(1)
		
		result = s.connect_ex((target,port)) # target is the argv 1, target we supply; port is the 50-85 range
		
		if result == 0: # means port is open, if it is closed equals one and goes back through the loop
			print(f"Port {port} is open")
		s.close() # close the socket connection on the closed port and go back through the loop on the next port in order
		
except KeyboardInterrupt:
	print("\nExiting Program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not connect to server.")
	sys.exit()
	 
