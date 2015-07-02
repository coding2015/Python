#!/usr/bin/python
#coding:utf-8

'''
modify Example 18.3
带锁的thread模块消耗时间最多
'''

import thread
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

def loop(nloop, num, lock):
	print 'start loop', nloop, 'at:', ctime()
	counting(num)
	print 'loop',nloop, 'done at:', ctime()
	lock.release()

def	main():
	print 'start at:', ctime()
	nloops = range(len(counts))
	locks = []	
	
	for i in nloops:
		lock = thread.allocate_lock()
		lock.acquire()
		locks.append(lock)
	
	for i in nloops:
		thread.start_new_thread(loop, (i, counts[i], locks[i]))
		
	for i in nloops:
		while locks[i].locked(): pass
	
	print 'all Done at:', ctime()


if __name__ == '__main__':
	main()


'''
start at: Thu Jul  2 06:34:31 2015
start loop start loop 01 at: Thu Jul  2 06:34:31 2015 
at: Thu Jul  2 06:34:31 2015
loop 0 done at: Thu Jul  2 06:34:49 2015
loop 1 done at: Thu Jul  2 06:34:56 2015
all Done at: Thu Jul  2 06:34:56 2015
'''
# total:25s  loop0:17s, loop1:25s
