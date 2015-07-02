#!/usr/bin/python
#coding:utf-8

'''
Example 18.8
	In this MT application, we excute threee seperate recursive functions.
	finst in a single-threaded fashion,
	followed by the alternative with multiple threads
'''

from myThread import MyThread
from time import ctime, sleep

def fib(x):
	sleep(0.005)
	if x < 2: return 1
	return (fib(x-1) + fib(x-2))

def fac(x):
	sleep(0.1)
	if x < 2: return 1
	return (x * fac(x-1))

def sum(x):
	sleep(0.1)
	if x < 2: return 1
	return (x + sum(x-1))

funcs = (fib, fac, sum)
n = 12

def main():
	nfuncs = range(len(funcs))
	
	print '*** SINGLE THREAD'
	for i in nfuncs:
		print 'staring', funcs[i].__name__, 'at:', ctime()
		print funcs[i](n)
		print funcs[i].__name__, 'finished at:', ctime()

	print '\n*** MULTIPLE THREADS'
	threads = []
	for i in nfuncs:
		t = MyThread(funcs[i], (n,), funcs[i].__name__) # (n,) ,means it's a tuple
		threads.append(t)
	
	for i in nfuncs:
		threads[i].start()

	for i in nfuncs:
		threads[i].join()
		print threads[i].getResult()

	for t in threads:
		print t.getName(), t.isAlive(), t.isDaemon()

	print 'all Done'

if __name__ == '__main__':
	main()		
		

'''
*** SINGLE THREAD
staring fib at: Thu Jul  2 09:30:47 2015
233
fib finished at: Thu Jul  2 09:30:49 2015
staring fac at: Thu Jul  2 09:30:49 2015
479001600
fac finished at: Thu Jul  2 09:30:51 2015
staring sum at: Thu Jul  2 09:30:51 2015
78
sum finished at: Thu Jul  2 09:30:52 2015

*** MULTIPLE THREADS
starting fib at: starting facThu Jul  2 09:30:52 2015 at: Thu Jul  2 09:30:52 2015
 starting
 sum at: Thu Jul  2 09:30:52 2015
fac sum finishing at: Thu Jul  2 09:30:53 2015
finishing at: Thu Jul  2 09:30:53 2015
fib finishing at: Thu Jul  2 09:30:54 2015
233
479001600
78
fib False False
fac False False
sum False False
all Done
'''

