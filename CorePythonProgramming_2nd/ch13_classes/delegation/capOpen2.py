#!/usr/bin/python
#coding:utf-8

'''
Exercise 13-16
	Wrap Standard Type, 包装文件对象
	writelines

'''

import os
EOF = os.linesep

class CapOpen(object):
	
	def __init__(self, fn, mode='r', buf=-1):
		self.fobj = open(fn, mode, buf)

	def __str__(self):
		return str(self.fobj)	# 返回文件状态
	
	def __repr__(self):
		return `self.fobj`

	def write(self, line):
		self.fobj.write(line.upper())

	def writelines(self, seq, addEOF=False):		
		self.fobj.writelines([('%s%s'% (line, EOF) if addEOF else line).upper() \
									for line in seq ])

	def __getattr__(self, attr):
		return getattr(self.fobj, attr)


'''
>>> f = cp2.CapOpen('xxx', 'w+')
>>> f.writelines(['heel', 'women', 'gentle'])
>>> f.seek(0)
>>> f.read()
'HEELWOMENGENTLE'
>>> 
>>> f.writelines(['children:', 'happy', 'initial'],True)
>>> f.seek(0)
>>> f.readlines()
['HEELWOMENGENTLECHILDREN:\n', 'HAPPY\n', 'INITIAL\n']

'''
