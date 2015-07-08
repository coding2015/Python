#!/usr/bin/python
#coding:utf-8
'''
Descriptor
研究点：
	描述符实例化 
	描述符作为实例属性
	描述符作为类属性
	属性优先级
'''
class Des:
	def __get__(self, instance, owner):
		print '__get__'
	def __set__(self, instance, value):
		print '__set__'
	def __delete__(self, instance):
		print '__delete__'


class Des(object):
	def __get__(self, instance, owner):
		print '__get__'

	def __set__(self, instance, value):
		print '__set__'

	def __delete__(self, instance):
		print '__delete__'

	def __repr__(self):
		# return `self` # rumtimeError, infinite recursion
		return 'repr invoked'


class C(object):
	d = Des()




# 单单的实例化描述符并无用处
'''
>>> d = Des()
>>> d
<__main__.Des object at 0x7fd51ca5dfd0>
>>> d = 12
>>> d
12
'''
# 描述符作实例的属性亦无用处(不会默认调用__get__等属性)
'''
>>> class B(object):pass
... 
>>> b = B()
>>> b.bd = de.Des()
>>> b.bd
repr invoked
'''
# 描述符作为类属性
'''
>>> c = de.C()
>>> c.d			# c.d == d.__get__(c, c.__class__) 
__get__		
>>> c.d = 12	# c.d=12 == d.__set__(c, 12)
__set__
>>> del c.d		# del c.d == d.__delete(c)
__delete__		
>>> c.d
__get__
'''
# 属性优先级
# 数据描述属性 > 实例属性
'''
>>> c.d
__get__
>>> c.d = 12
__set__
>>> c.__dict__
{}
>>> c.__dict__['d'] = 0
>>> c.__dict__
{'d': 0}
>>> c.d
__get__
>>> del c.d
__delete__
>>> c.d
__get__
>>> 
'''
# 类属性 > 数据描述符属性
'''
>>> c = de.C()
>>> c.d
__get__
>>> de.C.d = 'class-attr'
>>> c.d
'class-attr'
'''


