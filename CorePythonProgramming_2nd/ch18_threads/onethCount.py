#!/usr/bin/python
#coding:utf-8
'''
modify Example 18.1
测试：并发是否比串行节省时间
'''

from time import sleep, ctime

def counter(beg=0):
	count = [beg]
	def incr():
		count[0] += 1
	return incr

def counting(n):
	count = counter()
	for i in range(n): count()


def loop0():
	print 'start loop 0 at:', ctime()
	counting(19999999)	# 注意数字过大时内存会占满，然后电脑出现卡顿等情况
	print 'loop 0 done at:', ctime()

def loop1():
	print 'start loop 1 at:', ctime()
	counting(33333333)
	print 'loop 1 done at:', ctime()


def main():
	print 'starting at:', ctime()
	loop0()
	loop1()
	print 'all Done	at:', ctime()

if __name__ == '__main__':
	main()


'''
starting at: Wed Jul  1 19:43:50 2015
start loop 0 at: Wed Jul  1 19:43:50 2015
loop 0 done at: Wed Jul  1 19:43:54 2015
start loop 1 at: Wed Jul  1 19:43:54 2015
loop 1 done at: Wed Jul  1 19:44:01 2015
all Done	at: Wed Jul  1 19:44:01 2015
'''
#共花 4+7 = 11s
