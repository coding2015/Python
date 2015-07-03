#!/usr/bin/python
#coding:utf-8

'study for exception in thread'
'Problem: 结束子线程'

import threading 
import thread

class MyThread(threading.Thread):
	pass

def func(lock=None):
	print 'func()'
	while True: pass
#		try: pass
#		except KeyboardInterrupt:
#			print 'interrupt'
#			break
	if lock: lock.release()	
	print 'func() done'

def test1():
	func()


def test2():
	lock = thread.allocate_lock()
	lock.acquire()
	thread.start_new_thread(func, (lock,))
	while lock.locked():pass
	
def test3():
	t = threading.Thread(target=func)	
	t.start()
	while 1:
		try:
			#t.join()
			#while 1: pass
			t.join(block=False, timeout=0.5)
		except KeyboardInterrupt:
			print 'main recv interrupt'
			exit(-1)	
	

if __name__ == '__main__':
	test3()
