#!/usr/bin/python
#coding:utf-8

'''
经典类的__metaclass__
'''

class M(type):
	def __init__(cls, name, bases, attrd):
		print 'created class:', cls
		print '\tname:', name
		print '\tbases:', bases
		print '\tattrd:', attrd

class A:
	__metaclass__ = M
	def count(self):pass

'''
$ python classic.py 
created class: <class '__main__.A'>
	name: A
	bases: ()
	attrd: {'count': <function count at 0x7f8d69e9aa28>, '__module__': '__main__', '__metaclass__': <class '__main__.M'>}
'''
