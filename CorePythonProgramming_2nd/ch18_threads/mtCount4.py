#!/usr/bin/python
#coding:utf-8

'''
modify Example 18.5
callable class instance
'''

import threading
from time import sleep, ctime

def counter(beg=0):
	count = [beg]
	def incr():
		count[0] += 1
	return incr

def counting(n):
	count = counter()
	for i in range(n): count()

counts = [19999999, 33333333]

def loop(nloop, num):
	print 'start loop', nloop, 'at:', ctime()
	counting(num)
	print 'loop',nloop, 'done at:', ctime()


class ThreadFunc(object):
	'callable class'
	def __init__(self, func, args, name=''):
		self.func = func
		self.args = args
		self.name = name
	
	def __call__(self):
		self.func(*self.args)


def	main():
	print 'start at:', ctime()
	nloops = range(len(counts))
	threads = []	
	
	for i in nloops:
		t = threading.Thread(target=ThreadFunc(loop, (i, counts[i]),\
															 loop.__name__))
		threads.append(t)
	
	for i in nloops:
		threads[i].start()
		
	for i in nloops:
		threads[i].join()
	
	print 'all Done at:', ctime()


if __name__ == '__main__':
	main()


'''
start at: Thu Jul  2 08:10:36 2015
start loop 0 at: Thu Jul  2 08:10:36 2015
start loop 1 at: Thu Jul  2 08:10:36 2015
loop 0 done at: Thu Jul  2 08:10:48 2015
loop 1 done at: Thu Jul  2 08:10:51 2015
all Done at: Thu Jul  2 08:10:51 2015
'''
# total:15s  loop0:12s, loop1:15s
