#!/usr/bin/python
#coding:utf-8

'''
通过闭包描述符实现单例模式

单例模式：
		限制某类只能产生一个实例
		
KeyPoint:
	decorator, closure, shallow-copy(浅拷贝)
'''

def singleton(cls):

	instances = {}
	def getinstance():
		if cls not in instances:
			instances[cls] = cls()
			# print 'instance:', instances
		return instances[cls]
	
#	cells = getinstance.func_closure
#	print 'cells:', cells
#	if cells:
#		for e in cells:
#			print '\tcontents:',e.cell_contents

	return getinstance



@singleton		# -> A = singleton(A), 此时的A已经是singleton的闭包函数getinstance
class A:		# 之后的A() 实际为携带了自由变量的getinstance()
	pass

class C:
	pass


'''
test data:

>>> reload(sl)
cells: (<cell at 0x7f885e8bcec0: classobj object at 0x7f885e8bdf58>, <cell at 0x7f885e8dd0c0: dict object at 0x120cc80>)
	contents: singleton.A
	contents: {}
<module 'singleton' from 'singleton.py'>
>>> 
>>> a = sl.A()
instance: {<class singleton.A at 0x7f885e8bdf58>: <singleton.A instance at 0x7f885e8d45a8>}
>>> 
>>> a2 = sl.A()
>>> 
>>> a2 is a
True
>>> 
>>> c = sl.C()
>>> c2 = sl.C()
>>> c is c2
False

'''

