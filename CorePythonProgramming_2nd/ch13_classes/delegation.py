#!/usr/bin/python
#coding:utf-8

'''
Delegation:
	定制类： 
		新功能由定制类实现，已存在的功能授权给对象的默认属性
	授权关键：
		覆盖属性__getattr__, 在覆盖中调用内建函数 getattr(obj, attr)
	操作符:
		如[],*等不是属性，不能通过授权访问
		对此可直接返回对象后再进行操作

keyword:
	customization
	delegation

KeyPoint:
	__getattr__ 授权
'''


class Wrap(object):
	def __init__(self, obj):
		self.data = obj

	def __repr__(self):	#该属性类似init，不自定义来覆盖的话就会采用默认的
		print '__repr__() called'	#即就算不自定义也会在该类中找到此属性
		return `self.data`			#默认的返回为无多大意义的属性信息

	def __getattr__(self, attr):	#delegation
		print 'delegation: __getattr__(%s, %s)' %\
					(self.__class__.__name__, attr)
		return getattr(self.data, attr)
	
	def get(self):
		return self.data	#返回数据来直接访问对象属性，
							#包括授权不支持的对象操作符



#======test data========
#授权对象属性
'''
>>> wrList = delegation.Wrap([1,2])
>>> wrList
__repr__() called
[1, 2]
>>>
>>> wrList.append(69)
delegation: __getattr__(Wrap, append)
>>>
>>> wrList
__repr__() called
[1, 2, 69]
>>>
'''

#直接访问对象属性，尤其是不是属性的操作符
'''
>>> wrList * 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for *: 'Wrap' and 'int'
>>> 
>>> wrList.get() * 3
[1, 2, 1, 2, 1, 2]
>>>
>>> wrList[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'Wrap' object does not support indexing
>>> 
>>> wrList.get()[1]
2
>>> 
>>> wrList.get().append(23)
>>> 
>>> wrList
__repr__() called
[1, 2, 23]
'''


