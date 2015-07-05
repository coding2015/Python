#!/usr/bin/python
#coding:utf-8

'''
Exercise 13-7

Problem-Solved:
	how to print YY
Solving:
	gm.tm_year % 100 
'''

from time import *

def mdy(gm):
	'MM/DD/YY'
	print '%02d/%02d/%02d' % (gm.tm_mon, gm.tm_mday, (gm.tm_year % 100)) 

def mdyy(gm):
	'MM/DD/YYYY'
	print '%02d/%02d/%d' % (gm.tm_mon, gm.tm_mday, gm.tm_year)

def dmy(gm):
	'DD/MM/YY'
	print '%02d/%02d/%02d' % (gm.tm_mday, gm.tm_mon, (gm.tm_year % 100)) 

def dmyy(gm):
	'DD/MM/YYYY'
	print '%02d/%02d/%d' % (gm.tm_mday, gm.tm_mon, gm.tm_year) 

def modyy(gm):
	'Mon DD, YYYY'
	print '%s %02d, %d' % (MON[gm.tm_mon-1], gm.tm_mday, gm.tm_year)

MON = ('Jan','Feb','Mar','Apr','May','Jan','Jul','Aug','Sep','Oct','Nov','Dec')
FMT = {'MDY':mdy, 'MDYY':mdyy, 'DMY':dmy, 'DMYY':dmyy, 'MODYY':modyy}

class Time(object):
	def __init__(self):
		self.time = time()

	def __str__(self):
		return ctime(self.time)
	
	__repr__ = __str__

	#def update(self, t=time()): # 不能这么传默认值，在定义时值已定，调用时不会再赋值
	def update(self, t=None):
		if not t: t = time()
		self.time = t

	def display(self, fmt=None):
		if fmt in FMT:
			FMT[fmt](gmtime(self.time))
		else:
			print ctime(self.time)
	

'''
>>> t = ti.Time()
>>> t
Sun Jul  5 22:39:45 2015
>>> t.display('MDY')
07/05/15
>>> t.display('MDYY')
07/05/2015
>>> t.display('DMY')
05/07/15
>>> t.display('DMYY')
05/07/2015
>>> t.display('MODYY')
Jul 05, 2015
>>> t.update()
>>> t.display()
Sun Jul  5 23:06:09 2015
'''	
