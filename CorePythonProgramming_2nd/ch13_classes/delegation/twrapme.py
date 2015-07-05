#!/usr/bin/python
#coding:utf-8

'''
Example 13.7
	Wrapping Standard Types, 包装标准对象(给对象添加创建/修改/访问时间属性)
	Class definition that 
		wraps ant built-in types, adding time-attributes;
		get(), set(), and string representation methods; 
		and delegating all remaining attribute access to those of the standard types.

keyword:
	delegation
	wrap

应用/拓展：
	文件常见属性:创建时间, 修改时间，访问时间
	可以为对象添加这些属性以在特定场所提供额外信息
'''

from time import time, ctime

class TimedWrapMe(object):
	
	def __init__(self, obj):
		self.__data = obj
		self.__ctime = self.__mtime = self.__atime = time()
					# c:create, m:modify, a:access

	def get(self):
		self.__atime = time()	# 更新访问时间
		return self.__data

	def gettimeval(self, t_type):
		if not isinstance(t_type, str) or t_type[0] not in 'cma':
						# logic: 只要满足二者之一就raise TypeError
			raise TypeError, "argument of 'c', 'm', or 'a'"
		return getattr(self, '_%s__%stime' % (self.__class__.__name__, t_type[0]))
						# 相当于从类外访问getattr()访问私有变量 _类名__xxx

	def gettimestr(self, t_type):
		return ctime(self.gettimeval(t_type))

	def set(self, obj):
		self.__data = obj	# 类内访问私有变量
		self.__mtime = self.__atime = time() # 更新修改和访问时间

	def __repr__(self):
		self.__atime = time()	# 更新访问时间
		return `self.__data`

	def __str__(self):
		self.__atime = time() 	# 更新访问时间
		return str(self.__data)

	def __getattr__(self, attr):
		self.__atime = time()	# 更新访问时间
		return getattr(self.__data, attr)


'''
>>> import sys
>>> sys.path.append('delegation')
>>> import twrapme as gw
>>> t = gw.TimedWrapMe(123)
>>> t.gettimestr('a')
'Mon Jul  6 06:43:34 2015'
>>> t.gettimestr('c')
'Mon Jul  6 06:43:34 2015'
>>> t.gettimestr('m')
'Mon Jul  6 06:43:34 2015'
>>> t
123
>>> t.gettimestr('m')
'Mon Jul  6 06:43:34 2015'
>>> t.gettimestr('c')
'Mon Jul  6 06:43:34 2015'
>>> t.gettimestr('a')
'Mon Jul  6 06:43:56 2015'
>>> 
>>> t.gettimeval([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "delegation/twrapme.py", line 27, in gettimeval
    raise TypeError, "argument of 'c', 'm', or 'a'"
TypeError: argument of 'c', 'm', or 'a'
>>> 
>>> t.gettimeval('e')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "delegation/twrapme.py", line 27, in gettimeval
    raise TypeError, "argument of 'c', 'm', or 'a'"
TypeError: argument of 'c', 'm', or 'a'
>>>
>>> t.set('time is up')
>>> t.gettimestr('m')
'Mon Jul  6 06:49:39 2015'
>>> t
'time is up'
>>> t.gettimestr('c')
'Mon Jul  6 06:43:34 2015'
>>> t.gettimestr('m')
'Mon Jul  6 06:49:39 2015'
>>> t.gettimestr('a')
'Mon Jul  6 06:50:03 2015'
>>> 
>>> t.split()
['Time', 'is', 'up!']
>>> t.gettimestr('c')
'Mon Jul  6 06:43:34 2015'
>>> t.gettimestr('m')
'Mon Jul  6 06:49:39 2015'
>>> t.gettimestr('a')
'Mon Jul  6 06:53:56 2015'
'''	
