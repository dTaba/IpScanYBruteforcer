#!/usr/bin/python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket.AF_INET es ipv4 la ip y socket.SOCK_STREAM va a usar el protoclo tcp ip
socket.setdefaulttimeout(10)

host = input("[*]Enter the host to scan: ")

def portscanner(port):
	if sock.connect_ex((host,port)):
		print (colored("[!!]Port %d is closed" % (port),'red'))
	else:
		print (colored("[+]Port %d is opened" % (port),'green'))

for port in range(1,1000):
	portscanner(port)
