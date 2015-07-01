
'decorator and inner function'

def deco(func):
	print 'deco'
	def inner():
		print 'inner'
	return inner	# return inner-function


@deco
def foo():pass


foo()

'''
deco
inner
'''
