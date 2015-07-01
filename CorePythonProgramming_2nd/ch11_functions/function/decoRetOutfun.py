#!/usr/bin/python

'decorator and outside function'

def outfunc():
	print 'outside function'

def deco(func):
	print 'deco'
	return outfunc	# return outside-function


@deco
def foo():pass


foo()

'''
deco
outside function
'''
