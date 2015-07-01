
'closure'

def counter(start_at=0):
	count = [start_at]
	def incr():
		count[0] += 1
		return count[0]
	clo = incr.func_closure
	print 'clo[%d]:' % len(clo), clo
	return incr


'''
>>> count = cl.counter(10)
clo[1]: (<cell at 0x7fd040c506a8: list object at 0x7fd040c5b710>,)
>>> count()
11
>>> count()
12
>>> count()
13
>>> count2 = cl.counter(100)
clo[1]: (<cell at 0x7fd03f050e18: list object at 0x7fd03f048248>,)
>>> count2()
101
>>> count2()
102
>>> count2()
103
>>> count2()
104
'''
