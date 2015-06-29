"finally's exception overwrite the former exception"

try:
	try:
		float('er')
	finally:
		1/0
except BaseException,e:
	print 'out error:\t', e


'''
out error:	integer division or modulo by zero
'''
