#!/usr/bin/python 
#coding:utf-8

'''
Decorator and Closure:
	 Example 11.2
'''

from time import ctime

def tsfunc(func):
	def wrappedFunc():
		print '[%s] %s() called' % (ctime(), func.__name__)
		return func()
	return wrappedFunc

'''
>>> @dc.tsfunc
... def foo():
...     pass
... 
>>> for i in range(3):
...     time.sleep(2)
...     foo()
... 
[Wed Jul  1 08:17:52 2015] foo() called
[Wed Jul  1 08:17:54 2015] foo() called
[Wed Jul  1 08:17:56 2015] foo() called
'''
