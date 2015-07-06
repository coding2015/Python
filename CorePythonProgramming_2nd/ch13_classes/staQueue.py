#!/usr/bin/python
#coding:utf-8

'''
Exercise 13-10
	data structure that combines stack & queue 
	which can LIFO and FIFO 
'''

class StackQueue(object):
	
	def __init__(self):
		self.__data = []

	def shift(self):
		'return and remove the first item of the list'
		if hasattr(self.__data, 'pop'):
			ret = self.__data.pop(0)
		else:
			ret = self.__data[0]
			del self.__data[0]
		return ret

	def unshift(self, item):
		'add a new item to the head of the list'
		self.__data.insert(0, item)

	def push(self, item):
		'add a new item to the tail of the list'
		self.__data.append(item)

	def pop(self):
		'return and remove the tail item of the list'
		if hasattr(self.__data, 'pop'):
			ret = self.__data.pop()
		else:
			ret = self.__data[-1]
			del self.__data[-1]
		return ret
	
	def isempty(self):
		return False if len(self.__data) else True

	def view(self):
		print self.__data


'''
>>> import staQueue as sq
>>> st = sq.StackQueue()
>>> sq.__data
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute '__data'
>>> 
>>> st._StackQueue__data
[]
>>>
>>> st.push(23)
>>> st.push(10)
>>> st.push(9)
>>> st.view()
[23, 10, 9]
>>> st.unshift('head')
>>> st.unshift('buttom')
>>> st.view()
['buttom', 'head', 23, 10, 9]
>>> st.shift()
'buttom'
>>> st.shift()
'head'
>>> 
>>> st.pop()
9
>>> st.pop()
10
>>> st.pop()
23

'''
