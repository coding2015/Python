'continue in try-block'

while True:
	try:
		continue
	finally:
		print 'finally'


# output
'''
finally
finally
finally
finally
finally
finally
...

'''
