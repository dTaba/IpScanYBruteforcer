#!/usr/bin/python

import socket

def scanBanners(ip, port):
	try:
		socket.setdefaulttimeout(2)
        	s = socket.socket()
        	s.connect((ip, port))
        	banner = s.recv(1024)
		return banner
	except:
		return

def main():
	for port in range(0,100):
    		ip = raw_input("Ingresa la ip wachin: ")
		for port in range(0,100):
			banner = scanBanners(ip, port)
			if banner:
        			print 'Port ' + str(port) + " " + str(banner)
main()
