#!/usr/bin/python
#coding:utf-8

'''
Exercise 16-7:
	half duplex

Problem:
	1.线程里的server无法中断
	2.recv 阻塞
'''

import threading 
from time import ctime, sleep
from socket import *

def server():
	host = '127.0.0.1'
	port = 2000
	ADDR = (host, port)
	serSock = socket(AF_INET, SOCK_STREAM)
	serSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)	
	serSock.bind(ADDR)
	serSock.listen(1)
	
	try:
		print 'waiting for connecting...'
		cliSock,addr = serSock.accept()
		print '...connect from ', addr

		while True:
			data = raw_input('A send> ')	
			if not data:	# 不传非空数据，否则对方会一直阻塞等待
				break
			cliSock.send(str(data))
			data = cliSock.recv(1024) # 阻塞式等待数据，除非接收到数据或对方断开
			if not data:	# 此时对方已经断开连接
				print 'A recv:[%s] chat has interrupted...' % ctime()
				break
			else:
				print 'A recv:[%s] %s' % (ctime(), data)

		cliSock.close()
		del cliSock
	except (KeyboardInterrupt, EOFError):
		if 'cliSock' in dir():
			cliSock.close()
	
	serSock.close()
	print 'server has quitted'


def client():
	sleep(1)	# wait for server's preparation	

	host = '127.0.0.1'
	port = 2000
	ADDR = (host, port)
	cliSock = socket(AF_INET, SOCK_STREAM)	
	cliSock.connect(ADDR)

	while True:
		try:
			data = cliSock.recv(1024)
			if not data:
				print 'B recv:[%s] chat has interruputed' % ctime()
				break
			else:
				print 'B recv:[%s] %s' % (ctime(), data)
			data = raw_input('B send> ')
			if not data:
				break
			cliSock.send(data)
		except (EOFError, KeyboardInterrupt):
			break	

	cliSock.close()
	print 'B has quitted'

def main():
	print 'starting at:', ctime()
	threads = []
	peoples = (server, client)
	npeoples = range(len(peoples))
		
	for i in npeoples:
		t = threading.Thread(target=peoples[i])
		threads.append(t)

	for i in npeoples:
		threads[i].start()

	for i in npeoples:
		threads[i].join()

	print 'Done at:', ctime()

if __name__ == '__main__':
	main()


'''
starting at: Fri Jul  3 07:30:26 2015
waiting for connecting...
...connect from  ('127.0.0.1', 51462)
A send> hi
B recv:[Fri Jul  3 07:30:56 2015] hi
B send> hi
A recv:[Fri Jul  3 07:30:57 2015] hi
A send> how are you
B recv:[Fri Jul  3 07:31:04 2015] how are you
B send> fine, thank you. and you?
A recv:[Fri Jul  3 07:31:18 2015] fine, thank you. and you?
A send> i'm fine too.
B recv:[Fri Jul  3 07:31:34 2015] i'm fine too.
B send> ^_^
A recv:[Fri Jul  3 07:31:46 2015] ^_^
A send> :)
B recv:[Fri Jul  3 07:31:49 2015] :)
'''
