#coding:utf-8

'decorator with args'

def outfunc(x, y):
	print 'outfunc(%s, %s)' % (`x`, `y`)


def deco(func):
	print 'deco'
	return outfunc

@deco
def foo(): pass


foo(10,10)	# 实际参数传给了outfunc
'''
deco
outfunc(10, 10)
'''
