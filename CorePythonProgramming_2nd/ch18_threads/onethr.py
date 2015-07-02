#!/usr/bin/python

'Example 18.1'

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
	loop0()
	loop1()
	print 'all Done	at:', ctime()

if __name__ == '__main__':
	main()


'''
starting at: Wed Jul  1 17:54:08 2015
start loop 0 at: Wed Jul  1 17:54:08 2015
loop 0 done at: Wed Jul  1 17:54:12 2015
start loop 1 at: Wed Jul  1 17:54:12 2015
loop 1 done at: Wed Jul  1 17:54:14 2015
all Done	at: Wed Jul  1 17:54:14 2015
'''
