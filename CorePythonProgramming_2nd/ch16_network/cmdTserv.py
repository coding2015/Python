#!usr/bin/python
#coding:utf-8

'''
Exercise 16-5:
	TCP 服务端
		返回客户端的命令请求结果
		命令：
			date -> time.ctime()
			os -> os.name
			ls -> os.listdir('.')
			ls dir -> os.listdir(dir)

KeyPoint:
	str.split()
	str.strip()
	case-sensitive
'''

from socket import *
import os
from time import ctime

#dirname = '.'
#CMD = {'data':ctime(), 'os':os.name, 'ls':os.listdir(dirname)}
				#Error, 不能通过dirname来更新listdir的参数，该值已定

CMD_NONARG = {'os': os.name, 'data':ctime(), 'ls':os.listdir('.')}
CMD_ONEARG = {'ls':os.listdir}
ERROR_INFO = 'Invalid/Unsupport command'

def run(*args):
	if len(args):
		cmd = args[0]	
		N = len(args)
		if N == 1:
			return CMD_NONARG.get(cmd, ERROR_INFO)	#Eroor
				#TypeError: unhashable type: 'list'
				#调用run(data.split())时出错, data.split()是一个列表
		elif N == 2:
			if CMD_ONEARG.has_key(cmd):
				return CMD_ONEARG[cmd](args[1])
			else: return ERROR_INFO	#若无此句，隐式的else返回None
	else:
		return ERROR_INFO

serSock = socket(AF_INET, SOCK_STREAM)
serSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
ADDR = ('', 2100)
serSock.bind(ADDR)
serSock.listen(1)

while True:
	try:
		print 'wait for connect:'
		cliSock, addr = serSock.accept()
		print 'connecting from ', addr

		while True:
			data = cliSock.recv(1024)
			if not data:
				break
			#ret = run(data.split()) #！！solit()是一个列表，此时被作为一个元素
			ret = run(*(data.split())) #*提取序列各元素作为参数
			cliSock.send(str(ret))
		
		cliSock.close()		#when break
	except (EOFError, KeyboardInterrupt):
		print 'interrupt:'
		if 'cliSock' in vars():
			cliSock.close()
		break  #!!don't forget to leave the while

print 'out of while'
serSock.close()		#因为ctrl+c, ctrl+d 已经被捕获，故出了except之后会继续执行
					#可以在except中关闭服务器套接字，亦可出了while之后再关
	
