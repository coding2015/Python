#!/usr/bin/python
#coding:utf-8

'''
Intermediate Customization:

Example 13.5: anyIter.py
	reload next to return any number of items
'''

class AnyIter(object):
	
	def __init__(self, data, safe=False):
		self.iter = iter(data) #将序列转换为迭代器，以便在重载的next中调用next
		self.safe = safe
	
	def __iter__(self):
		return self

	def next(self, howmany=1):
		retval = []
		for i in range(howmany):
			try:
				#retval.append(self.data.next()) #Error:list has no ‘next’
				retval.append(self.iter.next())
			except StopIteration:
				if self.safe:
					break  #之后收到多少返回多少
				else:
					raise  #raise last exception
		return retval
