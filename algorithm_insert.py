#!/usr/bin/python
#coding:utf-8
'''
insert-algorithm
	比较，移位(腾出位置)，插入
	最坏的情况，原序列逆序，比较1+...n-1次，移动1+...n-1次，插入n-1次
	最好的情况：已排好序，比较n-1次，移动0次，插入0次
	时间复杂度0(n^2)
'''


def insert(a, reverse=False):
	'insert algorithm'
	N = len(a)
	if not reverse:
		for i in range(1,N):
			temp = a[i]
			#for j in range(i, 0, -1): #error:当首位移位时，首位索引(0)没有赋给j
			for j in range(i, -1, -1): 
				if a[j-1] > temp and j > 0:	#根据上一步j可以为0
												#故此需增加条件j>0 以防a[-1]咬尾
					a[j] = a[j-1] #move back a step 
									#and at next time j is the empty pos
				else:
					break 
			if j != i:
				a[j] = temp
	else:
		for i in range(1, N):
			temp = a[i]
			for j in range(i, -1, -1):
				if a[j-1] < temp and j>0:
					a[j] = a[j-1]
				else:
					break
			if j != i:
				a[j] = temp


	return a
