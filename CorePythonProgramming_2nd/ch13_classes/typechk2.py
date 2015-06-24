#!/usr/bin/python
#coding; utf-8

'''
typechk2.py
	判断某一实例是给定类型
		further study of type check
		earlier type check see in ch04
	
KeyPoint:
	isinstance(obj, Type)
		没有严格匹配：若obj是Type的子类实例，也返回True(预期应为False)
	is/is not: type(obj) is Type
		严格匹配
'''

#=====test data=====
>>> class P(object):pass
... 
>>> class C(P):pass
... 
>>> ct = C()
>>> 
>>>
>>> isinstance(ct, C)
True
>>> isinstance(ct, P) #不严格匹配
True 
>>> type(ct) is C
True
>>> type(ct) is P	#严格匹配
False
>>> 
>>>
>>> isinstance(C, ct)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: isinstance() arg 2 must be a class, type, or tuple of classes and types
>>> C is type(ct)
True
>>>
