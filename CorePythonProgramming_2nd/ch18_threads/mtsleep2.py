#!/usr/bin/python
#coding:utf-8

'''
Example 18.3
	Rather than using a call to sleep() to hold up the main thread as in mtsleep1.py,
the use of locks makes more sense
'''

import thread
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
	print 'start loop', nloop, 'at:', ctime()
	sleep(nsec)
	print 'loop', nloop, 'done at:', ctime()
	lock.release()

def main():
	print 'starting at:', ctime()
	locks = []
	nloops = range(len(loops))

	for i in nloops:
		lock = thread.allocate_lock()	
		lock.acquire()
		locks.append(lock)

	for i in nloops:
		thread.start_new_thread(loop, (i, loops[i], locks[i]))
		
	for i in nloops:	# 阻塞等待各子线程结束
		while locks[i].locked():pass

	print 'all Done at:', ctime()


if __name__ == '__main__':
	main()

'''
starting at: Thu Jul  2 06:06:35 2015
start loop 1 at: Thu Jul  2 06:06:35 2015start loop 
0 at: Thu Jul  2 06:06:35 2015
loop 1 done at: Thu Jul  2 06:06:37 2015
loop 0 done at: Thu Jul  2 06:06:39 2015
all Done at: Thu Jul  2 06:06:39 2015
'''
