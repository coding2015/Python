#!/usr/bin/python
#coding:utf-8

'Example 18.2'

import thread
from time import sleep, ctime

def loop0():
	print 'start loop 0 at:', ctime()
	sleep(4)
	print 'loop 0 done at:', ctime()

def loop1():
	print 'start loop 1 at:', ctime()
	sleep(2)
	print 'loop 1 done at:', ctime()


def main():
	print 'starting at:', ctime()
	thread.start_new_thread(loop0, ())
	thread.start_new_thread(loop1, ())
	sleep(6)	# 让当前线程(主线程)等待子线程结束后在运行下一句
	print 'all Done	at:', ctime()

if __name__ == '__main__':
	main()


'''
[ch18_threads 18:03 #204]$ python mtsleep1.py 
starting at: Wed Jul  1 18:03:32 2015
start loop 0 at: Wed Jul  1 18:03:32 2015
 start loop 1 at: Wed Jul  1 18:03:32 2015
loop 1 done at: Wed Jul  1 18:03:34 2015
loop 0 done at: Wed Jul  1 18:03:36 2015
all Done	at: Wed Jul  1 18:03:38 2015
'''
