#!/usr/bin/python
#coding:utf-8

'''
Example 13.9
	Using a File to Store an Attribute
	This class is crude but represents an interesting use of descriptors 
being able to store the contents of an attribute on the filesystem.

描述符应用: 通过文件系统保存属性内容
'''

import os
import pickle # 模块: 将对象串行字符串化

class FileDescr(object):
	'文件名对应属性名，文件内容对应属性内容'
	saved = []	# 用于保存注册了的属性名(文件名)

	def __init__(self, name=None):
		self.name = name


	def __get__(self, obj, typ=None):
		'访问注册了的属性内容'
		if self.name not in FileDescr.saved:
			raise AttributeError, "%r used before assignment" % self.name

		try:
			f = open(self.name, 'r')
			val = pickle.load(f) 
			f.close()
			return val
		except (pickle.UnpicklingError,IOError, EOFError, AttributeError,
					ImportError, IndexError), e:
			raise AttributeError, "could not read %r: %s" % (self.name, e)


	def __set__(self, obj, val):
		'创建属性文件并保存属性内容，然后注册属性名'
		f = open(self.name, 'w')
		try:
			try:
				pickle.dump(val, f) 
				FileDescr.saved.append(self.name) # 注册属性名
			except (TypeError, pickle.PicklingError), e:
				raise AttributeError, "could not pickle %r: %s" % (self.name, e) 
		finally:
			f.close()


	def __delete__(self, obj):
		'删除属性文件，并注销属性名'
		try:
			os.unlink(self.name)  # 删除属性文件
			FileDescr.saved.remove(self.name)	# 注销属性名
		except (OSError, ValueError), e:
			print '__delete__ error: ', e


'''
>>> class MyFileVarClass(object):
...     foo = descr.FileDescr('foo')
...     bar = descr.FileDescr('bar')
... 
>>> fvv = MyFileVarClass()
>>> print fvv.foo	
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/megan/Githubs/Python/CorePythonProgramming_2nd/ch13_classes/descriptor/descr.py", line 27, in __get__
    raise AttributeError, "%r used before assignment" % self.name
AttributeError: 'foo' used before assignment
>>> 
>>> fvv.foo = 42		# 注册'foo' 并保存 42
>>> fvv.bar = 'leanna'	# 注册'bar' 并保存 'leanna'
>>> print fvv.foo, fvv.bar
42 leanna
>>>
>>> del fvv.foo		# 注销'foo' 并删除其文件内容
>>> print fvv.foo, fvv.bar
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/megan/Githubs/Python/CorePythonProgramming_2nd/ch13_classes/descriptor/descr.py", line 27, in __get__
    raise AttributeError, "%r used before assignment" % self.name
AttributeError: 'foo' used before assignment
>>> 
>>> fvv.foo = __builtins__	# 试图串行化__builtins__到文件，并重新注册'foo'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/megan/Githubs/Python/CorePythonProgramming_2nd/ch13_classes/descriptor/descr.py", line 47, in __set__
    raise AttributeError, "could not pickle %r: %s" % (self.name, e) 
AttributeError: could not pickle 'foo': can't pickle module objects '
>>> 
>>> fvv.foo = 'hi'	# 串行化'hi'到文件，并重新注册'foo'
>>> print fvv.foo
hi
>>> 


'''		
