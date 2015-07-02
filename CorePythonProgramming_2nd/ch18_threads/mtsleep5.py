#!/usr/bin/python
#coding:utf-8

'''
Example 18.6
	Subclassing Thread  定制Thread子类
	Rather than instantiating the Thread class, we subclass it.
This gives us flexibility in customizing our threading objects and simplifies the
thread creation call.
'''

import threading
from time import ctime, sleep

loops = (4, 2)

class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self) # 父类初始化，进行必要的数据准备 
			# 必须初始化Thread, 否则报错
			# AssertionError: Thread.__init__() not called
		self.name = name
		self.func = func
		self.args = args

	def run(self):
		self.func(*self.args)
	
def loop(nloop, nsec):
	print 'start loop', nloop, 'at:', ctime()
	sleep(nsec)
	print 'loop', nloop, 'done at:', ctime()


def main():
	print 'starting at:', ctime()
	threads = []
	nloops = range(len(loops))

	for i in nloops:
		t = MyThread(loop, (i, loops[i]), loop.__name__)
		threads.append(t)
		
	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print 'all Done at:', ctime()

if __name__ == '__main__':
	main()


'''
starting at: Thu Jul  2 08:26:24 2015
start loop 0 at: Thu Jul  2 08:26:24 2015
start loop 1 at: Thu Jul  2 08:26:24 2015
loop 1 done at: Thu Jul  2 08:26:26 2015
loop 0 done at: Thu Jul  2 08:26:28 2015
all Done at: Thu Jul  2 08:26:28 2015
'''
