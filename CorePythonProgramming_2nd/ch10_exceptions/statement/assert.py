'assert statements'

# 1
assert 0
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
'''

# 2
assert 0, ('false', -1)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: ('false', -1)
'''

# 3
def isnumber(x):
	try:
		assert isinstance(x, (int, long, float, complex)), \
										 		'%s is not a number' % `x`
	except AssertionError, reason:
		#print '%s:\t%s' % (reason.__class__.__name__, reason)
		print repr(reason)
	else:
		print '%s is a number' % `x`

'''
>>> isnumber(23)
23 is a number
>>> 
>>> isnumber('hi')
AssertionError("'hi' is not a number",)

'''




