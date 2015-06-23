#!/usr/bin/python
#coding:utf-8

'''
若子类没有定义init，则创建子类实例时调用其父类init

类有实例没有的属性:
	__bases__
	__name__

类和实例都有的属性(值不同)
	__class__
	__doc__
'''

class P(object):
	'P class'
	def __init__(self):
		print 'in Parent init, created an instance of', \
				self.__class__.__name__ 
					 #实例没有__name__属性，需经由实例的对应的类来访问


class C1(P):
	pass
		

class C2(P):
	'Child2 class'
	def __init__(self):
		print 'in Child init, created an instance of', \
				self.__class__.__name__



pt = P()
print pt.__class__
# print pt.__bases__	# Error
		# AttributeError: 'P' object has no attribute '__bases__'
print pt.__class__.__bases__	 # 等价于P.__bases__
print pt.__doc__
print


print  'Child has not defined init'
ct = C1()
print ct.__class__
print C1.__bases__
print ct.__doc__
print

print  'Child has defined init'
ct = C2()
print ct.__class__
print C2.__bases__
print ct.__doc__
print




#=====Output======
'''
in Parent init, created an instance of P
<class '__main__.P'>
(<type 'object'>,)
P class

Child has not defined init
in Parent init, created an instance of C1
<class '__main__.C1'>
(<class '__main__.P'>,)
None

Child has defined init
in Child init, created an instance of C2
<class '__main__.C2'>
(<class '__main__.P'>,)
Child2 class

'''
