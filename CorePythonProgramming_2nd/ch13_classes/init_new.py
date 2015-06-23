#!/usr/bin/python
#coding:utf-8

'''
实验结果：
	class的方法参数必须包含self
	同时定义__init__ 和 __new__ 下实例化时只调用 __new__
	? 定义了__new__时，实例化对象是一个空类 NoneType
		？因为—__new__需要主动返回对象

Problem:
	不太理解__new__
'''
class MyClass(object):
	pass

mc = MyClass()
print type(mc)

class P(float):
	# def __init__(): #TypeError:参数少了self
	def __init__(self):
		print 'init'
	# def __new__():  #TypeError:参数少了self
	
	def __new__(self):
		print 'new'
		return self
	
	def fun(self):
		print 'fun'

pobj = P()
print type(pobj)	#NoneType
print type(P)
pobj.fun()  #AttributeError 'NoneType' object has attribute 'fun'


