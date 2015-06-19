#!/usr/bin/python

'''
Test:
	test for generator

generator function;
	make break point of function-excution by yield statement
	when call of the function, it returns a generator
	then you can process the function at break-points by generator.next()

generator expression:
	produce a generator:
		(expr for iter_val in iterable if conf_expr)
	similar to line comprehension (produce a list): 
		[expr for iter_var in iterable if conf_expr]

Problem:
	yeild:
		why var = (yield count) is None?
'''

def matrix_test():
	'''
	define and use of generator function and generator expression
	'''
	def cols(): # a simple generator
		yield 13
		yield 55
		yield 88
	rows = [1, 2, 3, 17]
	pairs = ((i, j) for i in rows for j in cols()) #generator expression
	for x in pairs:
		print x


def access_test():
	'''
	Access to generator (2 ways):
	1.generator.next() (raise StopInteration when it out of the generator's range)
	2.for loop (a smarter way without worry about StopInteration)
	'''
	def simpleGen():
		yield 1
		yield '2 --> punch'
	# 1.		
	gen = simpleGen()
	print gen.next()
	print gen.next()
	#print gen.next() #error: StopIteration, out of gen's range
	print

	# 2.
	for eachItem in simpleGen():
		print eachItem


def enhanced_test():
	'''
	Enhanced Generator Features:
		gen.send()
		gen.close()
	'''
	def counter(start_at=0):
		count = start_at
		while True:
			val = (yield count) #break point
			print 'val:', val	#None, why?
			if val is not None:
				count = val
			else:
				count += 1

	count = counter(5)
	print count.next()
	print count.next()
	print count.next()


enhanced_test()


