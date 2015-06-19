#!/usr/bin/python
'''
Test:
	a test for global variable
Conclude:
	in local area, 
		if there's no access of the global val before
			then define a local val with same name of global val is ok
		else
			it will occure UnboundLocalError

'''

glob = 12

#define a local val's name as global val
def func1():
	glob = 24
	print glob	#24


def func2():
	print glob	#12
	glob = 55	#UnboundLocalError
	print glob


def func3():
	glob += 1	#UnboundLocalError
				#glob = glob + 1
				#same as func2, it tries to access the global value 
				#and then assign to the local val

func3()
