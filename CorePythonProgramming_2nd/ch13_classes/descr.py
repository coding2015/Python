#!/usr/bin/python
#coding:utf-8

'''
Descriptor
	classes that define methods(attributes) as follow:
		__get__(self, instance, owner)	-> value
		__set__(self, instance, value)	-> None
		__delete__(self, instance)	-> None 
	描述符类型：
		数据描述符：同时覆盖了__get__与__set__的类
		非数据描述符：未覆盖__set__的类 
			凡是没有此属性的类都算非数据描述符
			亦可说所有的类分为两种：数据描述符，方法(非数据)描述符
	属性优先级别(Attribute Precedence)：
		类属性
		数据描述符
		实例属性
		非数据描述符
		__getattr__()

	Why：实例.属性，优先搜索自身属性。
			和以上优先级无关，而是就近搜索原则？

keyword:
	同名属性隐藏 hide

AddPoint:
	from __future__ import print_function
		print(*objects, sep=' ', end='\n', file=sys.stdout)	
	https://docs.python.org/2.7/library/functions.html?highlight=print#print 
'''

from __future__ import print_function

class NondataDescr(object):
	'descriptori: 非数据描述符(未定义)'
	def __get__(self, instance, owner):
		print('get(self, obj, owner):',
				 self, instance, owner, sep='\n') #future print()
	
	
class C1(object):
	attr = NondataDescr()	


class DataDescr(object):
	'descriptor:数据描述符'
	def __init__(self):
		print('__init__:', self) 

	def __get__(self, obj, owner):
		print('__get__:', self, obj, owner, sep='\n')
	
	def __set__(self, obj, value):
		print('__set__:', self, obj, value, sep='\n')

class C2(object):
	foo = DataDescr()    # 导入该模块时会调用__init__





#======test data=============
'''
>>> import descr as des
>>> reload(des)
__init__: <descr.DataDescr object at 0xe81090>
<module 'descr' from 'descr.py'>

'''
# NondataDescr and Subject
'''
>>> des.C1
<class 'descr.C1'>
>>> des.C1.attr
get(self, obj, owner):
<descr.NondataDescr object at 0xe81310>
None
<class 'descr.C1'>
>>> 
>>> c1 = des.C1()
>>> c1
<descr.C1 object at 0xe81810>
>>> c1.attr
get(self, obj, owner):
<descr.NondataDescr object at 0xe81310>
<descr.C1 object at 0xe81810>
<class 'descr.C1'>
>>>
>>> c1.__dict__
{}
>>> c1.attr = 12
>>> 
>>> c1.attr		# 非描述符属性<实例属性，非实例描述符属性被遮盖
12
>>> c1.__dict__
{'attr': 12}
'''

# DataDescr and C2
'''
>>> c2 = des.C2()
>>> c2.foo
__get__:
>>> 
>>> c2.__dict__
{}
>>> c2.foo = 12
__set__:
>>> c2.__dict__
{}
>>> c2.__dict__['foo'] = 24  # 定义实例属性
>>> c2.__dict__
{'foo': 24}
>>>
>>> c2.foo		# 描述符属性>实例属性,实例属性被遮盖
__get__:
>>> 
>>> c2.__dict__['foo']
24
>>>
>>> des.C2.foo
__get__:
>>>
>>> des.C2.foo = 'empty' # 类属性>数据描述符， 没有调用描述符的__set__
>>> des.C2.foo
'empty'
>>> c2.foo		# 类属性覆盖描述符后，实例属性还原本来面目
24 
'''



