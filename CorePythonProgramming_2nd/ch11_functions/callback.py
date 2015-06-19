#!/usr/bin/python
#coding:utf-8
'''
Test:
	a test for callback of closure
Problem:
	confuse:
		自由变量(为内部函数调用的外部函数变量) 的释放机制
		作为局部变量，难道不是应该调用完函数就被释放掉吗
		为何反而跟全局变量，对象一直存在呢？
'''


def counter(start_at=0):
	count = [start_at] #simulate a changable integer
	def incr():
		print 'inner:',count[0]
		count[0] += 1
		return count[0]
	return incr		#return a function-obj


def counterInt(start_at=0):
	count = start_at 
	def incr():
		count += 1   #UnboundLocalError
		return count
	return incr		


count = counter(1)
print count
print count()
print count()
print count()

count100 = counter(100)
print count100()
print count100()
print count100()


