#!/usr/bin/python
#coding:utf-8

'''
Queue:
	Producer-Constumer Problem, Example 18.9 
	We feature an implementation of the Producer-Consumer problem using Queue Objects
and a random number of good produced(and consumed). The producer and consumer are 
individually and concurrently executing threads.
'''

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread

def counter(start=0):
	count = [start]
	def incr():
		count[0] += 1
		return count[0]
	return incr

wcount = counter()
rcount = counter()

def writeQ(queue):
	n = wcount()
	print '[%d]producing object for Q...' % n
	queue.put('xxx', True)
	print '[%d] put end, size now'% n , queue.qsize()


def readQ(queue):
	n = rcount()
	print '[%d]consumed object from Q...' % n
	val = queue.get(True)
	print '[%d]' % n, 'get end:', val, 'size now', queue.qsize()


def writer(queue, loops):
	for i in range(loops):
		writeQ(queue)
		sleep(randint(1, 3)) # 比reader睡眠时间短，减少reader读取空队列而报错的机会


def reader(queue, loops):
	for i in range(loops):
		readQ(queue)
		sleep(randint(2, 5))


funcs = [writer, reader]
nfuncs = range(len(funcs))


def main():
	nloops = randint(2, 5)
	print 'nloops', nloops
	q = Queue(32)
		
	threads = []
	for i in nfuncs:
		t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:
		threads[i].start()
	
	for i in nfuncs:
		threads[i].join()

	print 'all Done'

if __name__ == '__main__':
	main()


'''
nloops 5
starting writer at: Thu Jul  2 10:37:30 2015
starting [1]producing object for Q...
reader at: Thu Jul  2 10:37:30 2015
[1] put end, size now 1
[1]consumed object from Q...
[1] get end: xxx size now 0
[2]producing object for Q...
[2] put end, size now 1
[3]producing object for Q...
[3] put end, size now 2
[2]consumed object from Q...
[2] get end: xxx size now 1
[4]producing object for Q...
[4] put end, size now 2
[3]consumed object from Q...
[3] get end: xxx size now 1
[5]producing object for Q...
[5] put end, size now 2
writer finishing at: Thu Jul  2 10:37:40 2015
[4]consumed object from Q...
[4] get end: xxx size now 1
[5]consumed object from Q...
[5] get end: xxx size now 0
reader finishing at: Thu Jul  2 10:37:50 2015
all Done
'''	
