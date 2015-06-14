#!/urs/bin/python

def displayNumType(num):
	'''
	displayNumType:
		 by isinstance()
	'''
	print num, 'is',
	if isinstance(num,(int,long,float,complex)):
		print 'a number of type:',type(num).__name__
	else:
		print 'not a number at all!!'


def displayNumType(num):
	'''
	displayNumType:
		evolution: 
			using the python way using "type(num)==type(0)...instead of isinstance()
	'''
	print num, "is",
	if type(num) == type(0):
		print 'an integer'
	elif type(num) == type(0L):
		print 'a long'
	elif type(num) == type(0.0):
		print 'a float'
	elif type(num) == type(0+0j):
		print 'a complex number'
	else:
		print 'not a number at all!!'


import types
def displayNumType(num):
	'''
	displayNumType: 
		impoved:
			reduce the times of calling type() by types.value
	'''
	print num, "is",
	if type(num) == types.IntType:
		print 'an integer'
	elif type(num) == types.LongType:
		print 'a long'
	elif type(num) == types.FloatType:
		print 'a float'
	elif type(num) == types.ComplexType:
		print 'a complex number'
	else:
		print 'not a number at all!!'


from types import IntType,LongType,FloatType,ComplexType
def displayNumType(num):
	'''
	displayNumType: 
		impoved:
			reduce the times of inquiring types.value by pre-import the values
	'''
	print num, "is",
	if type(num) == IntType:
		print 'an integer'
	elif type(num) == LongType:
		print 'a long'
	elif type(num) == FloatType:
		print 'a float'
	elif type(num) == ComplexType:
		print 'a complex number'
	else:
		print 'not a number at all!!'




#start
print displayNumType.__doc__
displayNumType(9999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
