#!/usr/bin/python
#coding:utf-8
from __future__ import division	 #__future__ must be imported at top of the file
'''
Exercise 11-9:
	create a average() using reduce

Process:
	不能用average来reduce，ie,不能用两两平均的方式迭代
		这就相当于先a与b对半，再对半后的b与c对半，...
		不能实现整体的平均
	先求和(reduce)再分配(平均)

KeyPoint:
	reduce()
'''

#from operator import add

def average(seq):
	#Sum = reduce(add, seq)
	Sum = reduce(lambda x,y:x+y, seq)
	return Sum/len(seq)


seq1 = [1, 2, 4, 5, 6, 12, 45]
seq2 = [5] * 6
seq3 = [3.1, 2.4, 5.6, 11.8]
sets = [seq1, seq2, seq3]
for seq in sets:
	print 'seq:', seq
	print 'average:%.2f' % average(seq)
	print


