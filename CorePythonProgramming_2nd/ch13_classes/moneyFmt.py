#!/usr/bin/python
#coding:utf-8

'''
Customization (Customizing Classes)

Exercise 13-3:
	String format class designed to 'wrap' floating point values 
	to appear as monetary amounts with appropriate symbols
'''

class MoneyFmt(object):
	def __init__(self, value=0.0):	
		self.value = float(value)

	
	def update(self, value=None):
		pass


	def __repr__(self):
		return `self.value`


	def __str__(self):
		'formatted display'
		pass

	
	def __nonzero__(self):
		'boolean test'
		pass

