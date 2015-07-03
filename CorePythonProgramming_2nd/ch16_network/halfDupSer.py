#!/usr/bin/python
#coding:utf-8

from socket import *
from time import ctime, sleep

def server():
    host = '127.0.0.1'
    port = 2000
    ADDR = (host, port)
    serSock = socket(AF_INET, SOCK_STREAM)
    serSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serSock.bind(ADDR)
    serSock.listen(1)

    while True:
        try:
            print 'waiting for connecting...'
            cliSock,addr = serSock.accept()
            print '...connect from ', addr

            while True:
                data = raw_input('A send> ')
                cliSock.send(str(data))
                data = cliSock.recv(1024)
                if not data:
                    print 'A recv:[%s] chat has interrupted...' % ctime()
                    break
                else:
                    print 'A recv:[%s] %s' % (ctime(), data)
            cliSock.close()
            del cliSock
        except (KeyboardInterrupt, EOFError):
			if 'cliSock' in dir(): cliSock.close()
			serSock.close()
			print 'A has quitted'
			break

if __name__ == '__main__':
	server()
