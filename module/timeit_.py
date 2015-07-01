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


def multi_timeit(funcs, showRetval=True, *vals): #!kwargs should be in front of *arg
	'''
	compare multy functions's time-elaspe, and print it in format
		funcs: a list of functions
		*vals: values for funcs' args
		showRetval: whether to show the func's return value
	usage:
		eg: multi_timeit(funcs, *(tuple/list))
	'''

	#nFormat = "%s(%s)".ljust(20) + ' time-elapse(%.5f)s'
		#can't relize the whole output's ljust here

	print 'type(vals):', type(vals)
	print 'vals:', vals
	
	for eachFunc in funcs:
		print '-' * 30
		for eachVal in vals:	
			ret = timeit(eachFunc, eachVal)
			if showRetval:
				Format = ("%s(%s) = %s" % \
						 (eachFunc.__name__, `eachVal`, ret[1])).ljust(30) \
						+ ' time-elapse(%.5f)s' % ret[0]
				print Farmat 
			else:
				nFormat = ("%s(%s):"%(eachFunc.__name__,`eachVal`)).ljust(20) \
						+ ' time-elapse(%.5f)s' % ret[0]
			
				print nFormat


	
#import self's module
import sys
#sys.path.append('/home/megan/Githubs/Python') #!must be the module's specific path
sys.path.append('/home/megan/Githubs/Python/CorePythonProgramming_2nd/ch08_loops')
import perfectNum

def test():
	funcs = (perfectNum.isperfect, perfectNum.perfectNums)
	vals = (6, 28,'496',10000)
	multi_timeit(funcs, False, *vals)


if __name__ == '__main__':
	test()

