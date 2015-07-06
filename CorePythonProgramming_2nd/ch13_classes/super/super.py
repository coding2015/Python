#!/usr/bin/python
#coding:utf-8

'''
Problem:
	难以理解__getattribute__
'''

class Base(object):
	def func(self):
		print '\tBase func(%s)' % self.__class__.__name__

	def bar(self):
		print '\tBase bar(%s)' % self.__class__.__name__

class P(Base):
	version = 1.0
	def func(self):
		print '\tP func()'

	def __getattribute__(self, attr):
		print '\tP get(%s)' % attr
		return super(P, self).__getattribute__(attr)

class C(P):
	version = 2.0

	def __init__(self, data=9):
		self.data = data

	def func(self):
		print '\tC func()'
		super(C, self).func()

	def __getattribute__(self, attr):
		print '\tC get(%s)' % attr
		return super(C, self).__getattribute__(attr)

	def test(self):
		super(self.__class__, self).func()	# 调用父类的func()
		super(self.__class__, self).bar()
		print '\tversion:', super(C, self).version


if __name__ == '__main__':
	c = C()
	#print 'main_test:'
	#c.func()	# 调用自己的func()
	#super(C, c).func()
	print 'c.attr:'
 	print '\tversion\n', c.version
	print '\tdata\n', c.data
	print '\nsupper.attr:'
	print '\tversion\n', super(C, c).version
	print '\tdata\n', super(C, c).data
	#c.bar()
	#super(c.__class__, c).func()
	#print '\tversion:', super(c.__class__, c).version

	print
	#print 'C_test:'
	#c.test()


# func()
'''
# c.func()
[super 17:28 #314]$ python super.py 
main_test:
	C get(func)
	P get(func)
	C func()
	P func()

# super(C.c).func()
[super 17:31 #315]$ python super.py 
main_test:
	P func()

# 观察: super().attr 没有调用__getattrbute__
		而且没有查找所属类属性，而是直接调用了父类属性
'''


# data and version
'''
c.attr:
	version
	C get(version)
	P get(version)
2.0
	data
	C get(data)
	P get(data)
9

supper.attr:
	version
1.0
	data
Traceback (most recent call last):
  File "super.py", line 50, in <module>
    print '\tdata\n', super(C, c).data
AttributeError: 'super' object has no attribute 'data'
'''
