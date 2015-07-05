#!/usr/bin/python
#coding:utf-8

'''
Example 13.8
	Wrap Standard Type, 包装文件对象，使写入所有字母大写
	Providing a file like object that customize the write() method
		while delegating the rest of the functionality to the file object.

应用：
	许多老式机器被限制只处理大写字母
'''

class CapOpen(object):
	
	def __init__(self, fn, mode='r', buf=-1):
		self.fobj = open(fn, mode, buf)

	def __str__(self):
		return str(self.fobj)	# 返回文件状态
	
	def __repr__(self):
		return `self.fobj`

	def write(self, line):
		self.fobj.write(line.upper())

	def __getattr__(self, attr):
		return getattr(self.fobj, attr)


'''
>>> import capOpen as cp
>>> f = cp.CapOpen('xxx', 'w')
>>> f.write('hello\n')
>>> f.write('this is a delegation example\n')
>>> f.write('it will upper all the input data into a file\n')
>>> f
<open file 'xxx', mode 'w' at 0x7f9087bcbc90>
>>> f.close()
>>> print f
<closed file 'xxx', mode 'w' at 0x7f9087bcbc90>
>>> 
>>> f = cp.CapOpen('xxx')
>>> f.read()
'HELLO\nTHIS IS A DELEGATION EXAMPLE\nIT WILL UPPER ALL THE INPUT DATA INTO A FILE\n'
>>>
>>> for line in f.readlines():
...     print line
... 
>>> f.seek(0)
>>> for line in f.readlines():
...     print line
... 
HELLO

THIS IS A DELEGATION EXAMPLE

IT WILL UPPER ALL THE INPUT DATA INTO A FILE

>>> f.seek(0)
>>> for line in f.readlines():
...     print line,
... 
HELLO
THIS IS A DELEGATION EXAMPLE
IT WILL UPPER ALL THE INPUT DATA INTO A FILE
>>> 
>>> os.unlink('xxx')	#  删除文件
'''
