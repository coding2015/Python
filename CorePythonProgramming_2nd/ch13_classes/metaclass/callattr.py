#!/usr/bin/python
#coding:utf-8

'''
metaclass.__call__(cls) -> instance of cls
'''

class M(type):
		def __init__(cls, name, bases, attrd):
			super(M, cls).__init__(name, bases, attrd) # 调用父类的__init__
			print 'class created', cls
	
		def __call__(cls, *args, **kw):  # 覆盖type的__call__
			print 'called class', cls, '(%r, %r)' % (args, kw)
			return super(M, cls).__call__(*args, **kw)	# 调用父类的__call__

class A(object):
	__metaclass__ = M
	
	def __init__(self, name=''):
		self.name = name
		print 'instance created', self
		
	#def __repr__(self):		# 若不定义将返回None, why? 不是继承了object吗
								# 分析错误，由于M.__call__没有返回
								# 故a = A() -> None, 即此时的a 并不是A的实例
		# return 'repr:', self # Error: 因为self 陷入infinit recursion,
		# super(A, self).__repr__()

'''
>>> reload(ca)
class created <class 'callattr.A'>	 # 导入模块时创建类
<module 'callattr' from 'callattr.py'>	
>>> a = ca.A()						
called class <class 'callattr.A'>  (('Jo',), {}) # 创建类实例时调用了元类的__call__
instance created <callattr.A object at 0x7f885e8ea550>
>>> a	  # 调用了object.__repr__(a)
<callattr.A object at 0x7f885e8ea550>
>>> a.name
'Jo'

'''



