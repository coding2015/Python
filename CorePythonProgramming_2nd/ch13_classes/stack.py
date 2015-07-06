#!/usr/bin/python
#coding:utf-8

'''
Exercise 13-8
	stack class, 堆栈类
	last-in-first-out  先进后出
'''

class Stack(object):
	def __init__(self):
		self.data = []

	def pop(self):
		'return and del the last item of the stack'
		if hasattr(self.data, 'pop'):
			ret = self.data.pop()
		else:
			ret = self.data[-1]
			del self.data[-1]
		return ret
	
	def push(self, item):
		'add item to the last'
		self.data.append(item)

	def isempty(self):
		'check if the stack is empty'
		return False if len(self.data) else True

	def peek(self):
		'return the top/last value of the stack'
		return self.data[-1] if len(self.data) else None
