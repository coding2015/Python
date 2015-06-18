#!/usr/bin/python

'''
Example 11.5:
	testit() invokes a given function with its arguments,
	returning True packed with the return value of the function on success
	or False with the cause of failture.

KeyPoint:
	variable-lenth arguments	

Problem:
	A = '%s' % x
	B = '%s' % `x`  
		when x is a non-str: A==B
		when x is a str: B has a pair of '' more than A
	why?
'''


def testit(func, *nkwargs, **kwargs):
	try:
		retval = func(*nkwargs, **kwargs) #!no matter what kind of arguments does
										#the func have, this format suits it.
		result = (True, retval)
	except Exception, diag:		#capture all kinds of Exception
		result = (False, str(diag))  #!diag is an instance of Exception
	return result


def test():
	funcs = (int, long, float)
	vals = (1234, 12.34, '1234', '12.34')
	
	for eachFunc in funcs:
		print '-' * 20		#repeat '-' 20 times
		for eachVal in vals:
			retval = testit(eachFunc, eachVal)
			if retval[0]:
				print '%s(%s) =' % (eachFunc.__name__, `eachVal`), retval[1]
				#``:when eachVal is a str, print output will add ``
			else:
				print '%s(%s) = FAILED:' % (eachFunc.__name__, `eachVal`), retval[1]

if __name__ == '__main__':
	test()
 
		

