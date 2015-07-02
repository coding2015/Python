#!/usr/bin/python
#coding:utf-8

'''
Example 18.4
	Using threading module
	The Thread class from the threading module has a join() method that
lets the main thread wait for thread completion
'''

import threading
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', ctime()
	sleep(nsec)
	print 'loop', nloop, 'done at:', ctime()

def main():
	print 'starting at:', ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = threading.Thread(target=loop, args=(i, loops[i]))
		threads.append(t)

	for i in nloops:	# 批量启动多线程
		threads[i].start()	

	for i in nloops:
		threads[i].join()	# wait for the thread to finish

	print 'all Done at:', ctime()


if __name__ == '__main__':
	main()
