#!/usr/bin/python
#coding:utf-8

'''
Exercise 13-9
	Queue class, 队列类
	first-in-first-out, 先进先出
'''


class Queue(object):
	'queue: first-in-first-out data structure'

	def __init__(self):
		self.__data = []

	def enqueue(self, item):
		'add new item to the tail of the list'
		self.__data.append(item)
	
	def dequeue(self):
 		'return and remove the head item of the list'
		if hasattr(self.__data, 'pop'):
			ret =  self.__data.pop(0)
		else:
			ret = self.__data[0]
			del self.__data[0]
		return ret
	
	def view(self):
		print self.__data

	def isempty(self):
		return False if len(self.__data) else True
