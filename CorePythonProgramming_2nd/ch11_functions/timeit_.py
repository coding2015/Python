#!/usr/bin/python

'''
Exercise 11-12:
	timeit():
		calculate the time of executing a given function with args.
		output: function's return value and time consuming.
		
KeyPoint:
	variable-lenth arguments
	time module
	import self module

Be careful of naming this file:	
	There's a timeit module in Python
	so don't name this file as timeit.py
		otherwise when you '$ pydoc timeit' in the current path
		it will go through this file instead of module timeit
		and produce a additional file named timeit.pyc 
		which make it always pydoc to this self-defined module
'''

#import Python's module
import time

def	timeit(func, *nkwargs, **kwargs):
	beg = time.time()
	try:
		retval = func(*nkwargs, **kwargs)
	except Exception, diag:
		retval = 'Failed:' + str(diag)
	end = time.time()
	time_elapsed = end - beg
	return (time_elapsed, retval)

	
#import self's module
import sys
#sys.path.append('/home/megan/Githubs/Python') #!must be the module's specific path
sys.path.append('/home/megan/Githubs/Python/CorePythonProgramming_2nd/ch08_loops')
import perfectNum

def test():
	funcs = (perfectNum.isperfect, perfectNum.perfectNums)
	vals = (6, 28,'496',10000)
	for func in funcs:
		print '-' * 30
		for val in vals:
			ret = timeit(func,val)
			#print '%s(%s) = %s, time-elapsed:%.2fs' % (func, `val`,ret[1],ret[0])
			print '%s(%s) = %s, time-elapsed(%.2fs)' % \
							 (func.__name__, `val`,ret[1],ret[0])


if __name__ == '__main__':
	test()

