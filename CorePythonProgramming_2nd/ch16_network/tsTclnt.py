#!/usr/bin/python
#coding:utf-8

'''
tsTclnt.py (Example 16.2):
	timestamp TCP client
	Creates a TCP client that prompts the user for message to send to the server,
	gets them back with a timestamp prefix, and displays the results to the user.
'''

from socket import *
from time import ctime

HOST = 'localhost'
#PORT = 21556	# 要与服务器端口一致，否则无法建立连接
				# 报错：socket.error: [Errno 111] Connection refused
PORT = 2000 
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	try:
		data = raw_input('> ')
		if not data:	# 若data的字节长度为0， 对方的recv()会一直处在阻塞等待中
			break 		
		#tcpCliSock.send('[' + ctime() + '] '+ data) #Error 理解错误
												#由服务端加上时间戳并返回
		tcpCliSock.send(data)
		data = tcpCliSock.recv(BUFSIZ)	# 无中断阻塞式等待数据，必须要接到数据才罢休
		if not data:	# 表示对方断开了连接
			break
		print data
	except (EOFError, KeyboardInterrupt):
		break	# 跳出死循环


tcpCliSock.close() #when-break and except-break

