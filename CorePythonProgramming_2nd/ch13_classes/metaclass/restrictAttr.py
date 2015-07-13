#!/usr/bin/python
#coding:utf-8

'''
Example 13.10
	create a metaclass that:
	1.forces programmers:
		to supply a __str__() method in their classes to provid useful messages
	2.strongly suggest programmers:
		override __repr__()	

metaclass application:
	providing template to define a class
'''

from warnings import warn

class ReqStrSugRepr(type):
	'metaclass that require overriding __str__ and suggest overriding __repr__'
	def __init__(cls, name, bases, attrd):
		super(ReqStrSugRepr, cls).__init__(name, bases, attrd)
		
		if '__str__' not in attrd:
			raise TypeError, "Class requires overriding of __str__()"

		if '__repr__' not in attrd:
			warn('Class suggests overriding of __repr__()\n', stacklevel=3)

print '*** Defined ReqStrSugRepr (meta)class\n'

class Foo(object):
	__metaclass__ = ReqStrSugRepr
	
	def __str__(self):
		return 'Instance of class:', self.__class__.__name__

	def __repr__(self):
		return self.__class__.__name__

print '*** Defined Foo class\n'

class Bar(object):
	__metaclass__ = ReqStrSugRepr
	
	def __str__(self):
		return 'Instance of class:', self.__class__.__name__

print '*** Defined Bar class\n'

class FooBar(object):		
	__metaclass__ = ReqStrSugRepr

print '*** Defined FooBar class\n'


'''
*** Defined ReqStrSugRepr (meta)class

*** Defined Foo class

sys:1: UserWarning: Class suggests overriding of __repr__()

*** Defined Bar class

Traceback (most recent call last):
  File "meta.py", line 50, in <module>
    class FooBar(object):		
  File "meta.py", line 24, in __init__
    raise TypeError, "Class requires overriding of __str__()"
TypeError: Class requires overriding of __str__()
'''
