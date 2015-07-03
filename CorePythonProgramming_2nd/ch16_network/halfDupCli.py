#!/usr/bin/python
#coding:utf-8

from socket import *
from time import ctime, sleep

def client():
    sleep(1)    # wait for server's preparation 

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
            cliSock.send(data)
        except (EOFError, KeyboardInterrupt):
            break

    cliSock.close()
    print 'B has quitted'


if __name__ == '__main__':
	client()
