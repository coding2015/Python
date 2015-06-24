#!/usr/bin/python
#coding:utf-8

'''
Class Customization

Exercise 13-5:
	Geometry:
		Point(x,y)
	Extra:
		overload: str, repr, add, sub, iadd, isub
'''

class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '(%d, %d)' % (self.x, self.y)
	
	__repr__ = __str__

	def __add__(self, other):
		return self.__class__(self.x + other.x,  self.y + other.y) 

	def __sub__(self, other):
		return self.__class__(self.x - other.x,  self.y -other.y)

	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self
