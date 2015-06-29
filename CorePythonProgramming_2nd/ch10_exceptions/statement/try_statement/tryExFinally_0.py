'''
异常上发
'''

try:
	try:
		1/0
	except TypeError, e:
		print 'type error', e
	finally:
		'finally'
except BaseException, e:
	print 'out error:\t', e



'''
'finally'
out error:	integer division or modulo by zero
'''
