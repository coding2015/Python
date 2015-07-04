#!/usr/bin/python
#coding:utf-8

'''
Example 11.8
	closure, decorator
'''

from time import time

def logged(when):

	def log(f, *args, **kwargs):
		print ''' called:
function: %s
args: %r
kwargs: %r''' % (f, args, kwargs)

	def pre_logged(f):
		def wrapped(*args, **kwargs):
			log(f, *args, **kwargs) 
			return f(*args, **kwargs)
		return wrapped

	def post_logged(f):
		def wrapped(*args, **kwargs):
			now = time()
			try:
				return f(*args, **kwargs)
			finally:
				log(f, *args, **kwargs)
				print 'time delta: %s' % (time()-now)
		return wrapped
	
	try:
		return {'pre':pre_logged, 'post': post_logged}[when]
	except KeyError, e:
		raise ValueError(e), 'must be "pre" or "post"'


@logged("post")
def hello(name):
	print "Hello", name
	return 3

print hello("World!")
		
'''
Hello World!
 called:
function: <function hello at 0x7f4703683aa0>
args: ('World!',)
kwargs: {}
time delta: 8.60691070557e-05
3
'''	
		
