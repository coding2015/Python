#!/usr/bin/python
#coding:utf-8

'''
Customization (Customizing Classes)

Exercise 13-3:
	String format class designed to 'wrap' floating point values 
	to appear as monetary amounts with appropriate symbols

KeyPoint:
	list.insert(index, ',') # insert comma before list[index]
	list.count('.')
	list.index('.')
'''

def dollarize(amount):
	
	#取绝对值
	isNegative = False
	if amount < 0:
		isNegative = True
		amount = abs(amount)

	#转换为列表来处理
	monL = list(str(round(amount,2))) #!当amount位数过多时格式为科学计数法:xxe+xx

	#insert comma ',' from end to beg
	if monL.count('.'):
		periodPos = monL.index('.') - len(monL) 
	else:
		periodPos = 0	
	insertPos = periodPos - 3
	while insertPos > -len(monL):  # not out of beg
		monL.insert(insertPos, ',')
		insertPos -= 1+3
		
	#insert money signs and negative signs
	monL.insert(0, '$')
	if isNegative:
		monL.insert(0, '-')

	return ''.join(monL)


class MoneyFmt(object):
	def __init__(self, value=0.0, showNegInPairs=False):	
		self.value = float(value)
		self.showNegInPairs = showNegInPairs #用尖括号表示负数
	
	def update(self, value=None):
		'replace the value with new one'
		if value is not None:
			self.value = value

	def __repr__(self):
		'display as a float'
		return `self.value`

	def __str__(self):
		'MoenyFmt - formatted display'
		amount = self.value
		isNegative = False
		if amount < 0:
			isNegative = True
			amount = abs(amount)
		monL = list(str(round(amount,2))) 

		if monL.count('.'): periodPos = monL.index('.') - len(monL) 
		else: periodPos = 0	
		insertPos = periodPos - 3
		while insertPos > -len(monL):  #condition: not out of beg
			monL.insert(insertPos, ',')
			insertPos -= 1+3		

		monL.insert(0, '$')
		if isNegative:
			if self.showNegInPairs:
				monL.insert(0,'<')
				monL.insert(len(monL), '>')
			else:
				monL.insert(0, '-')

		return ''.join(monL)

	
	def __nonzero__(self):
		'boolean test'
		if self.value :
			return True
		else:
			return False  	#include value None/0/0.0



