#!/usr/bin/python
#coding:utf-8

'''
Exercise 13-6
'''

from __future__ import division
import math

class Line(object):
	def __init__(self, p1, p0=(0.0, 0.0)):
		self.p1 = p1
		self.p0 = p0
	
	def __repr__(self):
		return `(self.p1, self.p0)`		

	def __str__(self):
		return str((self.p1, self.p0))

	def slope(self):
		ret = (self.p1[1] - self.p0[1])/(self.p1[0] - self.p0[0])
		return round(ret, 3)

	def length(self):
		ret = math.sqrt((self.p1[1] - self.p0[1])**2 + (self.p1[0] - self.p0[0])**2)
		return round(ret, 2)


'''
>>> lt = li.Line((19,8),(27,1))
>>> lt
((19, 8), (27, 1))
>>> lt.length()
10.63
>>> lt.slope()
-0.875
>>> 
>>> lt = li.Line((19,8))
>>> lt.length()
20.62
>>> lt.slope()
0.421
'''
