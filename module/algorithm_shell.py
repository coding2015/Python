#!/usr/bin/python
#coding:utf-8

'''
shell:
	an improved algorithm of insert
	间隔比较、移位、插入
	间隔：
		increment:[max,1]
		max_increment = len(n)/3 + 1
		increment = increment/3 + 1
	时间复杂度：0(n^(3/2))
'''


def shell(a, reverse=False):
	N = len(a)
	increment = N
	
	if not reverse:
		while(increment >= 1):
			increment = increment/3 + 1
			for i in range(increment, N, increment):
				temp = a[i]
				for j in range(i, -1, -increment):
					if a[j-increment] > temp and j-increment >= 0: #ascending order
						a[j] = a[j-increment]
					else:
						break			
				if j != i:
					a[j] = temp
			if increment == 1:
				break
	else:		
		while(increment >= 1):
			increment = increment/3 + 1
			for i in range(increment, N, increment):
				temp = a[i]
				for j in range(i, -1, -increment):
					if a[j-increment] < temp and j-increment >= 0: #descending order
						a[j] = a[j-increment]
					else:
						break			
				if j != i:
					a[j] = temp
			if increment == 1:
				break

	return a
