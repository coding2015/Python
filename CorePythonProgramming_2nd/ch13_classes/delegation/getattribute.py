#!/usr/bin/python
#coding:utf-8

'__getattrbute__ 属性只对新类起作用'
>>> class D:
...     version = 1.0
...     def __getattribute__(self, attr):
...             print '__getattribute__(%s)' % attr
... 
>>> D.version
1.0
>>> d = D()
>>> d.version
1.0
>>> d.x = 10
>>> d.x
10
>>>
>>> class A(object):
...     version = 1.0 
...     def __getattribute__(self, attr):
...             print '__getattribute__(%s)' % attr
...  
>>> 
>>> A.version
1.0
>>> a = A()
>>> a.version
__getattribute__(version)
>>> 
>>> a.x = 10
>>> a.x
__getattribute__(x)



'在__getattribute__()中访问实例的其他属性'
class B(object):
	def __init__(self, data=None):
		self.data = data
	def __getattribute__(self, attr):
		print '__get__', super(B, self).__getattribute__(attr) 

'''
对于
	def __getattribute__(self, attr):
			print self.attr		# 将陷入无穷递归
>>>b.data
>>>...
RuntimeError: maximum recursion depth exceeded while calling a Python object

对于
	def __getattribute__(self, attr):
		print '__get__', super(B, self).__getattribute__(attr) 

>>> c = C(12)
>>> c.data
__get__ 12

'''

class P(object):
	def __getattribute__(self, attr):
		print 'P get(%s)' % attr  

class C(object):
	def __init__(self, data=None):
		self.data = data
	def __getattribute__(self, attr):
		print 'C get(%s)' % attr , super(C, self).__getattribute__(attr) 

'''
>>> c = C(12)
>>> c.data
C get(data) 12
'''


