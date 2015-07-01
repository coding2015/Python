#coding:utf-8

'''
@deco1(deco_args)	#返回的对象也必须是一个装饰器
@deco2
@deco3
def func(args):pass
-> func = deco1(deco_args)(deco2(deco3(func)))

deco(deco_args) 
'''


def deco1(func):
	print 'deco1'
	def subdec(f):	
		print 'subdec'
		return f
	return subdec

def deco2(func):
	print 'deco2'
	def name(): pass
	return name

def deco3(func):
	print 'deco3'
	def name(): pass
	return name


@deco1(lambda:None)
@deco2
@deco3
def foo():pass

foo()

'''
deco1
deco3
deco2
subdec
'''


