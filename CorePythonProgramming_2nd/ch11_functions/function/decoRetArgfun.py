#!usr/bin/python
#coding:utf-8

'decorator'


def deco(func):
	print 'deco'
	return func	 # return argument-function

@deco
def foo():
	print 'foo'
foo()
'''
deco
foo
'''

print 

# @deco (def foo():block) 等价于 foo = deco(foo)
def bar():
	print 'bar'
bar = deco(bar)
bar()
'''
deco
bar
'''
