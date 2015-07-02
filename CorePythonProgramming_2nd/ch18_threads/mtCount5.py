#!/usr/bin/python
#coding:utf-8

'''
modify Example 18.6
定制Thread子类
'''

import threading
from time import sleep, ctime

counts = [19999999, 33333333]

def counter(beg=0):
	count = [beg]
	def incr():
		count[0] += 1
	return incr

def counting(n):
	count = counter()
	for i in range(n): count()

def loop(nloop, num):
	print 'start loop', nloop, 'at:', ctime()
	counting(num)
	print 'loop',nloop, 'done at:', ctime()

class MyThread(threading.Thread):
	'customizing Thread'
	def __init__(self, func, args, name=''):
		super(MyThread, self).__init__()
		self.func = func
		self.args = args
		self.name = name
	
	def run(self):
		self.func(*self.args)


def	main():
	print 'start at:', ctime()
	nloops = range(len(counts))
	threads = []	
	
	for i in nloops:
		t = MyThread(loop, (i, counts[i]))
		threads.append(t)
	
	for i in nloops:
		threads[i].start()
		
	for i in nloops:
		threads[i].join()
	
	print 'all Done at:', ctime()


if __name__ == '__main__':
	main()


'''
start at: Thu Jul  2 08:34:21 2015
start loop 0 at: Thu Jul  2 08:34:21 2015
start loop 1 at: Thu Jul  2 08:34:21 2015
loop 0 done at: Thu Jul  2 08:34:32 2015
loop 1 done at: Thu Jul  2 08:34:35 2015
all Done at: Thu Jul  2 08:34:35 2015
'''
# total:14s  loop0:11s, loop1:14s
