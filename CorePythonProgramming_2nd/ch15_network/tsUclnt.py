#!/usr/bin/python
#coding:utf-8

'''
tsUclnt.py (Example 16.4):
	timestamp UDP client
	Creates a UDP client that prompts the user for messages to send to the server
	, gets them back with a timestamp prefix, and displays them back to the user.
'''

from socket import *

HOST = 'localhost'
PORT = 21866
ADDR = (HOST, PORT)
BUFSIZ = 1024

udpCliSock = socket(type=SOCK_DGRAM)

while True:
	try:
		data = raw_input('> ')
		if not data:
			break
		udpCliSock.sendto(data, ADDR)
		data, ADDR = udpCliSock.recvfrom(BUFSIZ)
		if not data:
			break
		print data
	except (EOFError, KeyboardInterrupt):
		udpCliSock.close()
		break
