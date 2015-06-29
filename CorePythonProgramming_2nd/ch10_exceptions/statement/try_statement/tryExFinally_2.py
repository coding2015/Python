"exception lost"

def f():
	try:
		try:
			1/0
		finally:
			print 'finally'
			return
	except BaseException, e:
		print 'outside:\t', e


>>> f()
'finally'

