#!/usr/bin/python

'a test for try-except-finally'

#
def OverWrite():
	try:
		try:
			float('xx')
		finally:
			float({}) 
	except (ValueError, TypeError),r:
		print 'r:',r    #print exception from finally
						#and the former exception has been lost


def Break():
	try:
		try:
			float('xx')
		finally:
			return	# end of this function, and the exception isn't processed
			float({}) 
	except (ValueError, TypeError),r:
		print 'r:',r


#OverWrite()
#Break()

while True:
	try:
		try:
			float('xx')
		finally:
			break # end of this loop, and the exception isn't processed
			float({}) 
	except (ValueError, TypeError),r:
		print 'r:',r

