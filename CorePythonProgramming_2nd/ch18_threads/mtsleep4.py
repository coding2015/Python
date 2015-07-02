#!/usr/bin/python
#coding;utf-8

'''
Example 18.5:
	使用可调用类对象作为target
	Using Callable classes instead of function. 
	In this example we pass in a callable class(instance) as opposed to 
just a function. It presents more of an OO approach than mtsleep3.py
'''

import threading
from time import sleep, ctime

loops = [4, 2]

class ThreadFunc(object):
	'callable class'
	def __init__(self, func, args, name=''):
		self.name = name
		self.func = func
		self.args = args

	def __call__(self):
		# apply(self.func, self.args)
		self.func(*self.args)

def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', ctime()
	sleep(nsec)
	print 'loop', nloop, 'done at:', ctime()


def	main():
	print 'starting at:', ctime()
	nloops = range(len(loops))
	threads = []

	for i in nloops:
		t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print 'all Done at:', ctime()

if __name__ == '__main__':
	main()
	
	
'''
starting at: Thu Jul  2 07:53:59 2015
start loop 0 at: Thu Jul  2 07:53:59 2015
start loop 1 at: Thu Jul  2 07:53:59 2015
loop 1 done at: Thu Jul  2 07:54:01 2015
loop 0 done at: Thu Jul  2 07:54:03 2015
all Done at: Thu Jul  2 07:54:03 2015
'''	
