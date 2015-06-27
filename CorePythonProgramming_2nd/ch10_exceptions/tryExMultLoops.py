#!/usr/bin/python
#coding:utf-8

'''
study try-except in double-loop
即使在多层循环中
	只要try 语句监控的是内几层的循环
	一旦出现异常，且被except捕获，就可在except中退出整个循环
'''

def loop():
	while True:
		try:
			ft = float(raw_input('> '))
		except (ValueError, TypeError, KeyboardInterrupt, EOFError),e:
			print 'e:',e
			break	#！！无该句无法退出

def multiloop():
	while True:
		try:
			while True:
				while True:
					ft = float(raw_input('> '))
		except (ValueError, TypeError, KeyboardInterrupt, EOFError),e:
			print 'e:',e
			break				


