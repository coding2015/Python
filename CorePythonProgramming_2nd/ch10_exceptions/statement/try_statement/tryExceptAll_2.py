'catch all exceptions'

try:
    1/0
except:
    print 'except'
	import sys
	print sys.exc_info()


'''
except
(<type 'exceptions.ZeroDivisionError'>, ZeroDivisionError('integer division or modulo by zero',), <traceback object at 0x7fd040c4f248>)
'''

