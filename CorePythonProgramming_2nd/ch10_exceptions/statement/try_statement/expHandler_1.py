try:
	try:
		try:
			1/0
		except TypeError,e:
			print '1.TypeError:',e
	except ValueError, e:
			print '2.ValueError:',e
except ZeroDivisionError, e:
	print '3.ZeroDivisionError:',e


'''
3.ZeroDivisionError: integer division or modulo by zero
'''
