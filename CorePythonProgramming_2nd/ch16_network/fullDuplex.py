#!/usr/bin/python
#coding:utf-8

'''
Exercise 16-8:
	full duplex  全双工

Problem:
	1.如何关闭客户端套接字
	 通过[cliSock], del cliSoc的方法不管用

'''

import threading 
from time import ctime, sleep
from socket import *

def reciever(sock, who):
	while True:
		if not sock[0]:
			break
		data = sock[0].recv(1024)
	 	if not data:
			print '%s recv:[%s] chat has interrupted...' % (who, ctime())
			break
		print '%s recv:[%s] %s' % (who, ctime(), data)
  
def sender(sock, who):
	while True:
		if not sock[0]:
			break
		data = raw_input('%s send> '% who)	
		if not data:
			break
		sock[0].send(str(data))

funcs = [sender, reciever]
nfuncs = range(len(funcs))

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
	
		threads = []
		for i in nfuncs:
			#t = threads.Thread(target=funcs[i], args=([cliSock], 'A')) #error
			t = threading.Thread(target=funcs[i], args=([cliSock], 'A'),\
												name=funcs[i].__name__)
			threads.append(t)

		for i in nfuncs:
			threads[i].start()

		exc = False
		while True:
			for i in nfuncs:
				sleep(0.5)
				if not threads[i].isAlive():
					print 'A-', threads[i].getName(),'has dead'
					exc = True
					break  # 只能退出for循环
					#cliSock.close() #error
		#UnboundLocalError: local variable 'cliSock' referenced before assignment
					#del cliSock		
			if exc:
				break			

	except (KeyboardInterrupt, EOFError):
		pass
		
	if 'cliSock' in dir():
		print 'A close cliSock'
		cliSock.close()
		del cliSock
	serSock.close()
	print 'server has quitted'


def client():
	sleep(1)	# wait for server's preparation	

	host = '127.0.0.1'
	port = 2000
	ADDR = (host, port)
	cliSock = socket(AF_INET, SOCK_STREAM)	
	cliSock.connect(ADDR)

	try:
		threads = []
		for i in nfuncs:
			t = threading.Thread(target=funcs[i], args=([cliSock], 'B'),\
									name=funcs[i].__name__)
			threads.append(t)

		for i in nfuncs:
			threads[i].start()

		exc = False
		while True:
			for i in nfuncs:
				sleep(0.5)
				if not threads[i].isAlive():
					print 'B-', threads[i].getName(),'has dead'
					exc = True
					break
			if exc: 
				break
	except (EOFError, KeyboardInterrupt):
		pass	

	cliSock.close()
	del cliSock
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
