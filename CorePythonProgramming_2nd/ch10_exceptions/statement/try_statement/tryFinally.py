def fun():
    try:
        x = 1/0
		print 'continue...'
    finally:
        return 9


>>> fun()
9

