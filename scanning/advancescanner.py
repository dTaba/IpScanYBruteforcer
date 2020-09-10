#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(tgtHost, tgtPort):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((tgtHost,tgtPort))
		print '[+] %d/tcp is Open' % tgtPort
	except:
		print '[-] %d/tcp is Closed' % tgtPort
	finally:
		sock.close()

def portScan(tgtHost, tgtPorts):
	try:
		tgtIp = gethostbyname(tgtHost)
	except:
		print 'Unknown Host %s' %tgtHost
	try:
		tgtName = gethostbyaddr(tgtIp)
		print '[+] Scan results for: ' + tgtName[0]
	except:
		print '[+] Scan results for: ' + tgtIp
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()

def main():
	parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>') #Printeo uso del programa
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host') #Agrego las opciones que mencione antes al parser
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
	(options, args) = parser.parse_args() #Defino que argumentos va a tener la variable parser que cree mas arriba
	tgtHost = options.tgtHost #Creo la variable y la vinculo con el tgtHost de la opcion del parser
	tgtPorts = str(options.tgtPort).split(',') 
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()

