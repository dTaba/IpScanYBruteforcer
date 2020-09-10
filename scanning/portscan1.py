#!/usr/bin/python

import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket.AF_INET  es ipv4 la ip y socket.SOCK_STREAM va a usar el protoclo tcp ip

host = raw_input("[*]Enter the host to scan: ")
port = raw_input("[*]Enter the port to scan: ")

def portscanner(port):
	if sock.connect_ex((host,port)):
		print "[!!]Port %d is closed" % (port)
	else:
		print "[+]Port %d is opened" % (port)

portscanner(port)
