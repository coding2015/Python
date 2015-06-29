#!/usr/bin/python
#coding:utf-8

'''
singleton:
	单例模式：
		限制某类只能产生一个实例

KeyPoint:
	decorator
'''

def singleton(cls):
	'''
	preserve only one class type,
	and return only one class instance.
	'''
	instances = {}
	def getinstance():
		if cls not in instances:
			instances[cls] = cls()
			print 'instance:', instances
		return instances[cls]
	
	return getinstance


@singleton
class A:
	pass

@singleton
class B:
	pass

class C:
	pass


'''
test data:

>>> reload(sl)
<module 'singleton' from 'singleton.py'>
>>> 
>>> a1 = sl.A()
>>> a2 = sl.A()
>>> a2 is a1
True
>>> 
>>> b1 = sl.B()
>>> b2 = sl.B()
>>> b2 is b1
True
>>> 
>>> c1 = sl.C()
>>> c2 = sl.C()
>>> c2 is c1
False



'''

