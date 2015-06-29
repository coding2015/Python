"exception lost due to break in finally-block"

while True:
	try:
		try:
			1/0
		finally:
			print 'finally'
			break
			#continue   #Error: 'continue' not supported inside 'finally' clause
	except BaseException, e:
		print 'outside:\t', e


'''
finally
'''

