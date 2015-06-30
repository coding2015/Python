#!/usr/bin/python
#coding: utf-8

'''
tsTserv.py (Example 16.1):
	timestamp TCP server (TCP时间戳服务器)
	creating a TCP server:
		creates a TCP server that accepts messages from clents and returns them
	with a timestamp prefix.
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21556
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcpSerSock = socket()	#创建套接字，socket参数取其默认值

#tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)	
		#在未解除绑定的情况(比如服务器退出而客户端未退出)，重新运行服务器会报错
		#socket.error: [Errno 98] Address already in use
		#需在约5分钟内系统才清除绑定，释放端口资源
		#而调用此句将告诉内核重新使用处于TIME_WAIT状态的套接字，不需等待资源释放

tcpSerSock.bind(ADDR)	#绑定套接字到服务器地址
tcpSerSock.listen(5)	#允许同时5个连接

'''
依次处理一个连接
若同时有多个连接请求
只有当当前连接断开后才去处理下一个连接
'''
while True:
	try:
		print 'waiting for connection...'
		tcpCliSock, addr = tcpSerSock.accept()	#阻塞式监听，
				#若有客户端发起连接请求,返回一个代表的连接的套接字和客户端地址
		print  '...connected from:', addr

		while True:
			data = tcpCliSock.recv(BUFSIZ) #等待客户发送数据
			if not data:
				break	 #problem, 隐患，按此设计，break后不会关闭套接字
			else:
				tcpCliSock.send('[%s] %s' % (ctime(), data)) #返回数据给客户
		tcpCliSock.close()
	except (EOFError, KeyboardInterrupt): #ctrl+d 无反应，why? 
										#ctrl+d正常， 客户端对此异常有反应
		if 'tcpCliSock' in vars():
			print 'close tcpClient'
			tcpCliSock.close()	#试验了重复关句柄(socket,file)没有异常								#Problem:是否存在可以判断socket已关闭的方法
					#另外，即使在此关闭了客户端套接字，但连接仍未断开，why?	
		tcpSerSock.close()
		break

