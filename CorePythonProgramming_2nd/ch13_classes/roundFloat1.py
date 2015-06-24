#!/usr/bin/python
#coding:utf-8

'''
Junior Customization:
	inherit from standard type of Python
	standard type:
		immutable: numerical(int, float, ...)
		mutable:   dict, list
KeyPoint:
	__new__(cls, args)
		类方法， 不同于实例方法__init__(self）

'''


class RoundFloat(float):
	'immutable-type example'
	def __new__(cls, val):
		print 'RoundFloat.__new__(%s, %s)' % (cls.__name__, val)
		# return float.__new__(cls, round(val. 2))
		return super(RoundFloat, cls).__new__(cls, round(val, 2))


class SortedKeyDict(dict):
	'mutable type example'
	def keys(self):
		return sorted(super(SortedKeyDict,self).keys())


def testRoundFloat():
	print RoundFloat(1.341)
	print RoundFloat(1.345)
	print RoundFloat(1.346)

	print RoundFloat(-2.123)
	print RoundFloat(-2.125)
	print RoundFloat(-2.127)

	print type(RoundFloat(1.2))


def testSortedKeyDict():
	d1 = {'jone':89, 'zen':100, 'jane':78} #dict type
	d2 = SortedKeyDict(d1) #SortedKeyDict type
	print ('d1 (%s):'% type(d1).__name__).ljust(20), [key for key in d1]
	print ('d2 (%s):'% type(d2).__name__).ljust(20), d2.keys()


#=====Output=======
'''
d1 (dict):           ['jane', 'zen', 'jone']
d2 (SortedKeyDict):  ['jane', 'jone', 'zen']
'''

#======Output======
'''
RoundFloat.__new__(RoundFloat, 1.341)
1.34
RoundFloat.__new__(RoundFloat, 1.345)
1.34
RoundFloat.__new__(RoundFloat, 1.346)
1.35
RoundFloat.__new__(RoundFloat, -2.123)
-2.12
RoundFloat.__new__(RoundFloat, -2.125)
-2.13
RoundFloat.__new__(RoundFloat, -2.127)
-2.13
RoundFloat.__new__(RoundFloat, 1.2)
<class '__main__.RoundFloat'>

'''


''
