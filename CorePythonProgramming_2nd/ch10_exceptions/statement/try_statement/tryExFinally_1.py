"finally's exception overwrite former exception"

try:
	try:
		float('er')
	except ValueError, e:
		print 'inner error:\t', e
	finally:
		1/0
except BaseException,e:
	print 'out error:\t', e


'''
inner error:	could not convert string to float: er
out error:	integer division or modulo by zero
'''
