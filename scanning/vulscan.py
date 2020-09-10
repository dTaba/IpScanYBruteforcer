#!/usr/bin/python

import socket
import os
import sys


def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, archivo):
	f = open(archivo, "r")
	for line in f.readlines():
		if line.strip("\n") in banner:
			print '[+] Vulnerabilidad encontrada '+ banner.strip("\n")
def main():
	if len(sys.argv) == 2:
	 	archivo  = sys.argv[1]
		if not os.path.isfile(archivo):
			print '[-] No existe el archivo'
			exit(0)
		if not os.access(archivo, os.R_OK):
			print '[-] Acceso denegado fiera'
			exit(0)
	else:
		print 'Modo de uso ' + sys.argv[0] + '<archivodevulnerables>'
		exit(0)

	portlist = [21, 22, 25, 80, 110, 443, 445]
	for i in range(20,23):
		ip = '192.168.0.' + str(i)
		for port in portlist:
			banner = retBanner(ip, port)
			if banner:
				print '[+]' + ip + '/' + str(port) + ':' + banner
				checkVulns(banner, archivo)
main()
