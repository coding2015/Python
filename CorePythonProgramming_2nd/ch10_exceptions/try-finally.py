#!/usr/bin/python
#coding:utf-8
'''
Study try-except-finally:
	finally:
		如果finally中引发另一个异常或终止循环(break/continue)或退出函数(continue)，
	则原来的异常将被覆盖或丢失。
'''

#
def OverWrite():
	try:
		try:
			float('xx')
		finally:
			float({}) 
	except (ValueError, TypeError),r:
		print 'r:',r    #print exception from finally
						#and the former exception has been lost


def Break():
	try:
		try:
			float('xx')
		finally:
			return	# end of this function, and the exception isn't processed
			float({}) 
	except (ValueError, TypeError),r:
		print 'r:',r


#OverWrite()
#Break()


while True:
	try:
		try:
			float('xx')
		finally:
			#break # !end of this loop, and the exception isn't processed
			float({}) 
	except (ValueError, TypeError),r:
		print 'r:',r
		break


#=====Output=====
'''
r: float() argument must be a string or a number
'''
