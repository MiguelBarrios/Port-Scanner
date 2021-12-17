import pyfiglet
import sys
import socket
from datetime import datetime
from termcolor import colored, cprint


banner = pyfiglet.figlet_format("PORT SCANNER")
cprint(banner, 'green')

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

target = socket.gethostbyname(local_ip)

print("Scanning : " + target)
print("Scan started : " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		if s.connect_ex((target,port)) == 0:
			print("Port {} is open".format(port))
		s.close()
except:
	print("error");
