#!/usr/bin/python
#coding:utf-8

'''
Exercise 16-5:
	客户端
'''

from socket import *

cliSock = socket(AF_INET, SOCK_STREAM)
ADDR = ('localhost',2100)
cliSock.connect(ADDR)

while True:
	try:
		cmd = raw_input('cmd> ')
		if not cmd:
			break
		cliSock.send(cmd)
		ret = cliSock.recv(1024)
		print ret
	
	except (EOFError, KeyboardInterrupt):
		print 'interrupt'
		break

cliSock.close()	#包括break出来的情况，故出了except再关
		
