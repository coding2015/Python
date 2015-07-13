#!/usr/bin/python
#coding:utf-8

'''
通过元类实现单例模式
'''

class Singleton(type):
	def __init__(cls, name, bases, attrd):
		super(Singleton, cls).__init__(name, bases, attrd)
		cls.instance = None
	
	def __call__(cls, *args, **kws):
		if not cls.instance:
			cls.instance = super(Singleton, cls).__call__(*args, **kws)
		return cls.instance


class A(object):
	__metaclass__ = Singleton


class B(object):
	pass


'''
>>> a = sl.A()
>>> a2 = sl.A()
>>> a is a2
True
>>> 
>>> b = sl.B()
>>> b2 = sl.B()
>> b is b2
False
'''
