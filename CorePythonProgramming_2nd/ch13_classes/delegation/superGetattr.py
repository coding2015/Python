#!/usr/bin/python
#coding:utf-8

'''
__getattribute__ & super():

super(type, obj).__getattribute__(attr) == object/parent.__getattribute__(obj, attr)
按__mro__顺序从obj开始搜寻属性

super(xxx, type2/obj).attr
找的是xxx父类的属性（亦按__mro__进行搜寻，但掠过xxx及其继承者们）
'''

class B(object):
	time = 2015
	
	def func(self):
		print 'B func invoked'

class P(B):
	version = 0.0
	count = 99
	def __init__(self, data=-12):
		print 'P init invoked'
		self.data = data

	def bar(self):
		print 'P func invoked'
	
	def __getattribute__(self, attr):
		print 'P getattribute invoked'
		return object.__getattribute__(self, attr)

class C(P):
	version = 1.0
	def __init__(self, data=10):
		super(C, self).__init__()
		self.data = data
	
	def func(self):
		print 'C func invoked'

	def __getattribute__(self, attr):
		print 'C getattibute invoked'
		# return C.__getattribute__(self, attr) # RuntimeError, infinite recursion
		# return P.__getattribute__(self, attr)
		return object.__getattribute__(self, attr)
		# return super(B, C).__getattribute__(self, attr)
		# return super(B, P).__getattribute__(self, attr)
		# return super(B, self).__getattribute__(attr)
		# return super(C, self).__getattribute__(attr)


if __name__ == '__main__':
	c = C()
	print c.data
	print '-'*30
	print c.version	
	print '-'*30
	print c.count	
	print '-'*30
	print c.time
	print '-'*30
	c.func()
	print '-'*30
	c.bar()
	print '-'*30
	object.__getattribute__(c, 'func')()
	print '-'*30
	B.__getattribute__(c, 'bar')()
	print '-'*30
	print P.__getattribute__(c, 'time')

	print '#'*30
	super(P, C).func(c)
	print '-'*30
	super(C, c).func()
	print '-'*30
	# super(P, C).bar(c)	# AttributeError: 'super' object has no attribute 'bar'
	super(C, c).bar()
	print '-'*30
	# print super(B, c).count #AttributeError 'super' object has no attribute 'count'
	print super(C, c).count
	print '-'*30
	print super(P, C).time
	print '-'*30



'''

P init invoked
C getattibute invoked
10
------------------------------
C getattibute invoked
1.0
------------------------------
C getattibute invoked
99
------------------------------
C getattibute invoked
2015
------------------------------
C getattibute invoked
C func invoked
------------------------------
C getattibute invoked
P func invoked
------------------------------
C func invoked
------------------------------
P func invoked
------------------------------
P getattribute invoked
2015
##############################
B func invoked
------------------------------
B func invoked
------------------------------
P func invoked
------------------------------
99
------------------------------
2015
------------------------------
'''
