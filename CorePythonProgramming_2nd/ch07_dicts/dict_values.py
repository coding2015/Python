#!/usr/bin/python
#coding:utf-8

'''
Exercise 7-3, 7-7
	字典: 按键值排序并访问键值对

思路(两种)：
一：
	取键值列表排序
	按键值访问键值对
二：
	另外创建一个字典：以原字典的键值为键，键为内容
	对新建字典键排序，之后按该键序访问键值对

延伸：
	比较两者性能(时间消耗)
	结果表明： 第二种方式性能更好(第一种的耗时是第二种的20倍左右)
'''

def valueList(dic):
	vlist = dic.values()
	vlist.sort()
	for e in vlist:
		for k in dic:		# 时间被耗在了遍历找键的过程
			if e == dic[k]:
				(k, e)


def newDict(dic):
	newdict = {}
	for k in dic:
		newdict[dic[k]] = k

	keys = newdict.keys()
	keys.sort()
	for k in keys:
		(k, newdict[k])	 	# 直接访问，不需遍历


# 观察性能
import timeit
import gendata

dic = gendata.dic(100)
valueList(dic)
newDict(dic)

print '\ntime elapse'
valueTimer = timeit.Timer('valueList(dic)',"from __main__ import valueList,dic")
newTimer = timeit.Timer('__main__.newDict(__main__.dic)',"import __main__")
for i in [1, 10, 100, 1000, 10000]:
	t1 = valueTimer.timeit(number=i)
	t2 = newTimer.timeit(number=i)
	print '\ntimes(%d)' % i
	print '\tvalueList:', t1
	print '\tnewTimer: ', t2
	print '\tvalue/new:', t1/t2

'''
$ python dict_values.py 

time elapse

times(1)
	valueList: 0.000816106796265
	newTimer:  4.29153442383e-05
	value/new: 19.0166666667

times(10)
	valueList: 0.00817894935608
	newTimer:  0.00032901763916
	value/new: 24.8586956522

times(100)
	valueList: 0.0817141532898
	newTimer:  0.00320291519165
	value/new: 25.5124311449

times(1000)
	valueList: 0.81253695488
	newTimer:  0.0322420597076
	value/new: 25.2011491278

times(10000)
	valueList: 8.51740098
	newTimer:  0.352902889252
	value/new: 24.1352543133
'''





