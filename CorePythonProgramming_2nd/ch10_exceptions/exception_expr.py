#!/urs/bin/python

'a test for try-exception expresses'

def safe_float(obj):
	try:
		return float(obj)
	# except ValueError,TypeError: # Error, multy-Errors should put in a tuple
	except (ValueError, TypeError), r :
		print 'r:',r
		print 'type(r):', type(r)
		print 'argument should be a number or numeric string'

print 'non-number:'
safe_float('non-num')
print
print 'non str/num type:'
safe_float({})

