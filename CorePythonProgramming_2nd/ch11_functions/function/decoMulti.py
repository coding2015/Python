
'''
@deco1
@deco2
def func():pass
-> func = deco1(deco2(func))
'''

def deco1(func):
	print 'deco1'
	def name():pass
	return name

def deco2(func):
	print 'deco2'
	def name():pass	
	return name

@deco1
@deco2
def foo():pass

foo()

'''
deco2
deco1
'''
