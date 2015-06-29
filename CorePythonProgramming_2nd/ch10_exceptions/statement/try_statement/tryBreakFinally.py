'break in try-block'

while True:
    try:
        break
		1/0
	except:
		print 'except'
	else:
		print 'else'
    finally:
        print 'finally'
                      
'''
finally
'''


