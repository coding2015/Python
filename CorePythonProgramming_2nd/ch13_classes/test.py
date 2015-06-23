#!/usr/bin/python
#coding:utf-8

'''
define a class as test data
	Python 没有重载，即使是在类中，后定义的类方法也会覆盖其之前定义的同名函数
'''

class Test(object):
	version = 1.0
	d = {'key':'value'}
	
	def __init__(self): # 永远不会被调用：已被以下定义的同名函数覆盖
		print 'Test.__init__(self)'

	def __init__(self, count):
		self.count = count
		print 'Test.__init__(%s, %s)' % (self, count)	


	def func(self):
		print 'func() called'


class SubTest(Test):
	def __init__(self, count):
		Test.__init__(self, count)	# 若不显示调用,则不会自动调用父类init
		print 'SubTest.__init__(%s, %s)'	% (self, count)


def test():
	st = SubTest(23)
	print st.version
		

if __name__ == '__main__':
	test()
	
