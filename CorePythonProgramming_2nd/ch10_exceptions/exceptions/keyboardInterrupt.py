

def foo():
	while 1:
		try: pass
		except KeyboardInterrupt:
			print 'interrupt'
			break

'''
>>> foo()
^Cinterrupt
>>> foo()		# KeyboardInterrupt 没有被捕获
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in foo
KeyboardInterrupt
>>> foo()
^Cinterrupt

'''


def bar():
	while 1:
		try: raw_input('> ')
		except KeyboardInterrupt:
			print 'interrupt'
			break

'''
>>> bar()
> interrupt
'''	
 

def double():
	from time import sleep
	while 1:
		try: 
			sleep(2)
			try: sleep(3)
			except KeyboardInterrupt:
				print '1'
				break
		except KeyboardInterrupt:
			print '2'
			break
'''
>>> double()
^C2
>>> double()
^C2
>>> double()
^C1
>>> double()
^C2
>>> double()
^C1
'''

