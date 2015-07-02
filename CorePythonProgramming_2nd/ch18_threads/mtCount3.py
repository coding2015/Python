#!/usr/bin/python
#coding:utf-8

'''
modify Example 18.4
测试时间仍比串行长， 但优于带锁的thread模块时间
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


def	main():
	print 'start at:', ctime()
	nloops = range(len(counts))
	threads = []	
	
	for i in nloops:
		#t = threading.Thread(loop, (i, counts[i])) #error, 
			# AssertionError: group argument must be None for now
		t = threading.Thread(target=loop, args=(i, counts[i]))
		threads.append(t)
	
	for i in nloops:
		threads[i].start()
		
	for i in nloops:
		threads[i].join()
	
	print 'all Done at:', ctime()


if __name__ == '__main__':
	main()


'''
start at: Thu Jul  2 07:27:34 2015
start loop 0 at: Thu Jul  2 07:27:34 2015
 start loop 1 at: Thu Jul  2 07:27:35 2015
loop 0 done at: Thu Jul  2 07:27:45 2015
loop 1 done at: Thu Jul  2 07:27:48 2015
all Done at: Thu Jul  2 07:27:48 2015
'''
# total:14s  loop0:11s, loop1:13s
