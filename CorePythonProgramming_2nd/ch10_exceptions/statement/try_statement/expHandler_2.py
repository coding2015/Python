try:
	float([1])
	#1/0
except (ValueError, TypeError),e:
	print 'specify error:', e
except BaseException, e:
	print 'other error:', e


'''
specify error: float() argument must be a string or a number
'''


'''
other error: integer division or modulo by zero
'''

