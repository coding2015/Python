#!/usr/bin/python
#coding: utf-8

'''
diamond construction of multi-inheritance:
	 /\
	 \/ 

'''

class B(object):
	pass

class C(object):
	def __init__(self):
		print 'C.__init__ called'

class D(B, C):
	pass


d = D()
print D.__mro__


#=====Output======
# classic-classes 
#  	| |
#  	\/
'C.__init__ called'

# new-style-classes
#	/\
#	\/
'''
C.__init__ called
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <type 'object'>)
'''
