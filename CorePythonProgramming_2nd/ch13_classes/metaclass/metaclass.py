#!/usr/bin/python
#coding:utf-8

'''
metaclass  and __metaclass__
'''

from __future__ import print_function

print('*** Metaclass declaration first')
class MetaC(type):
	def __init__(cls, name, bases, attrd):
		super(MetaC, cls).__init__(name, bases, attrd)
		# -> type.__init__(cls,name, bases, attrd)
		print ('\tCreated class', name)	
		print('\tcls: '+`cls`, 'name: '+`name`, 'bases: '+`bases`,\
					 'attrd: '+`attrd`, sep='\n\t')
	
print('*** Class "Foo" declaration next')
class Foo(object):
	__metaclass__ = MetaC
	version = 1.0
	def __init__(self):pass


'''
*** Metaclass declaration first
*** Class "Foo" declaration next
	Created class Foo
	cls: <class '__main__.Foo'>
	name: 'Foo'
	bases: (<type 'object'>,)
	attrd: {'__module__': '__main__', 'version': 1.0, '__metaclass__': <class '__main__.MetaC'>, '__init__': <function __init__ at 0x7f41af41fcf8>}
'''
