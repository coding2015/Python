#!/usr/bin/python
#coding:utf-8
'''
静态方法
	不能调用静态方法的原函数名	
		由类调用静态方法的原函数名会被视为没有实例化
		由实例调用静态方法的原函数名会被视为传入了多余的参数(实例本身)
	调用静态方法名
		由实例调用静态方法，python不会自动将实例传入静态方法
	
keypoint
	staticmethod(function) -> method
	classmethod(function) -> method, \
					function至少带一个参数用于接收解释器自动传入的类名

	usage(2 ways):
		1.assignment
			after define the function:	
				fun = staticmethod(fun)
		2.decorator
			before define the function use decorator(@...):
				@classmethod
				def fun(cls,...):
					pass	
'''

def globalfun():
	print '\tglobal function'

class StM():

	def cfun():
		print '\tcfun()'	
	
	def cfuns(self):
		print '\tcfuns(%s)' % self
	
	CF = staticmethod(cfun)
	CFs = staticmethod(cfuns)
	Glo = staticmethod(globalfun)

	
	@classmethod
	def foo(cls):	# 至少得有一个变量，否则不能类方法化
		print '\tfoo(%s)' % cls
	
	#foo = classmethod(foo)	#调用时解释器自动将类传给foo的第一个参数

def test():	
	s = StM()

	print '1.<<<staticmethod()>>>'
	print 'class.static():'
	StM.CF()
	# print 'class.origin():'
	# StM.cfun()	# Error \
	# TypeError: unbound method cfun() must be called with StM instance as first argument (got nothing instead)
	print 'instance.static():'
	s.CF()
	# print 'instance.origin():'
	# s.cfun()		# Error \
	# TypeError: cfun() takes no arguments (1 given)
	print
	
	print '2.<<<staticmethod(arg)>>>'
	print 'class.static(arg):'
	StM.CFs(12)	
	print 'class.origin(arg):'
	StM.cfuns(s)
	print 'instance.static(arg):'
	s.CFs(24)
	print 'instance.origin(arg):'
	s.cfuns()
	print

	print '3.<<<static(globalfun)>>>'	
	print 'class.static()'
	StM.Glo()
	print 'instance.static()'
	s.Glo()
	print

	print '4.<<<classmethod>>>'
	print 'class.classmethod(cls)'
	StM.foo()
	print 'instance.classmethod(cls)'
	s.foo()

if __name__ == '__main__':
	test()



#=====OutPut=====
'''
1.<<<staticmethod()>>>
class.static():
	cfun()
instance.static():
	cfun()

2.<<<staticmethod(arg)>>>
class.static(arg):
	cfuns(12)
class.origin(arg):
	cfuns(<__main__.StM instance at 0x7f0622440440>)
instance.static(arg):
	cfuns(24)
instance.origin(arg):
	cfuns(<__main__.StM instance at 0x7f0622440440>)

3.<<<static(globalfun)>>>
class.static()
	global function
instance.static()
	global function

4.<<<classmethod>>>
class.classmethod(cls)
	foo(__main__.StM)
instance.classmethod(cls)
	foo(__main__.StM)

'''
