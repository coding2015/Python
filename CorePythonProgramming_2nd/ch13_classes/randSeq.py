#!/usr/bin/python
#coding: utf-8

'''
Junior Customization
	Example 13.4: randSeq.py

	不同于Python的next(), 该模块重载的next()永远不会引起StopIteration异常

KeyPoint:
	定制迭代器
	next() overload
'''

from random import choice


class RandSeq(object):
	
	def __init__(self, seq):
		'RandSeq constructor - takes a sequence'
		self.data = seq

	def __iter__(self):
		'RandSeq -declare the object as an iterator'
		return self

	def next(self):
		'RandSeq - get the value of the iterator and reaches no end '
		return choice(self.data)


	
	
