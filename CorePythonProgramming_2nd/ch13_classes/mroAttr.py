#!/usr/bin/python
#coding:utf-8
'''
Multiple Inheritance:
	Method Resolution Order (MRO)

KeyWord:
	Attribute

KeyPoint:
	new-style-class.__mro__   查看新类的搜索顺序
'''

class P1(object): # parent class 1
	def foo(self): 
		print 'called P1-foo()' 

class P2(object): # parent class 2
	def foo(self): 
		print 'called P2-foo()' 
	def bar(self): 
		print 'called P2-bar()' 

class C1(P1, P2): # child 1 der. from P1, P2
	pass 

class C2(P1, P2):	# child 2 der. from P1, P2
	def bar(self):
		print 'called C2-bar()'

class GC(C1, C2):	# define grandchild class
	pass			# derived from C1 and C2


gc = GC()
gc.foo()
gc.bar()

print GC.__mro__ # only new-style classes have this attribute

#=====Output=======
# classic classes: the root class doesn't inherit from any class
'''
called P1-foo()
called P2-bar()
'''
# new-style classes: the root class inherit from other class, like 'object'
'''
called P1-foo()
called C2-bar()

(<class '__main__.GC'>, <class '__main__.C1'>, <class '__main__.C2'>, <class '__main__.P1'>, <class '__main__.P2'>, <type 'object'>)
'''
