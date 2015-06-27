#!/usr/bin/python
#coding:utf-8

'''
tsUserv.py (Example 16.3)
	timestamp UDP server
	Creates a UDP server that accepts messages from clients 
	and returns them with a timestamp prefix.
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21866
ADDR = (HOST, PORT)
BUFSIZ = 1024

udpSerSock = socket(type=SOCK_DGRAM)
udpSerSock.bind(ADDR)

'''
不需建立连接
可以同时接收并发送数据到多个客户端
'''
while True:
	try:
		print 'waiting for message...'
		data, addr = udpSerSock.recvfrom(BUFSIZ)
		udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
		print '...recieved from and returned to:', addr
	except (EOFError, KeyboardInterrupt): #ctrl+d 亦无反应，why? 对应客户端正常
		udpSerSock.close()
		break


