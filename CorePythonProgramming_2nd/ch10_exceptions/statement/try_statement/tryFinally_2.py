'return in finally-block overwrite return in other blocks'

def f():
	try:
		return 'try'
	finally:
		return 'finally'


>>> f()
'finally'

