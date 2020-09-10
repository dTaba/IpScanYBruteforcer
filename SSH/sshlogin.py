#!/usr/bin/python

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def main():
	host = raw_input('Ingresa el host: ')
	usuario = raw_input('Ingresa el usuario: ')
	contrasena = raw_input('Ingresa la contrasena: ')
	consolassh = conexionssh(usuario, host, contrasena)
	enviarcomando('cat /etc/shadow | grep root', consolassh)

def conexionssh(usuario, host, contrasena):
	sshclave = 'Are you sure you want to continue connecting'
	connstr = 'ssh ' + usuario + '@' + host
	consolaresultante = pexpect.spawn(connstr)
	resultado = consolaresultante.expect([pexpect.TIMEOUT, sshclave, '[P|p]assword: '])
	print 'El resultado del primer expect es ' + str(resultado)
	if resultado == 0:
		print '[-] Error conectando'
		return
	elif resultado == 1:
		consolaresultante.sendline('yes')
		resultado = consolaresultante.expect([pexpect.TIMEOUT, '[P|p]assword: '])
		if resultado == 0:
		 	print '[-] Error conectando'
                	return
	consolaresultante.sendline(contrasena)
	consolaresultante.expect(PROMPT)
	return consolaresultante

def enviarcomando(comando, consola):
	consola.sendline(comando)
	consola.expect(PROMPT)
	print consola.before

if __name__ == "__main__":
	main()
