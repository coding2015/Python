#!/usr/bin/python
#coding:utf-8

'''
generate data for test
'''

from string import letters
from random import randint, choice


def dic(size, strlen=3):
	'''
	generate a given size dict
	key: randint
	value: a random letters of strlen length
	'''
	d = {}
	i = 0
	while i < size:
		# 产生随机键
		key = randint(0, 1000)
		if key in d: continue	# 若k已存在，就舍弃
		else: i += 1
	
		# 产生随机键值
		temp = []
		#for i in range(strlen):	# error 覆盖了while的i
		for j in range(strlen):
			temp.append(choice(letters))
		value = ''.join(temp)
		
		# 添加键值对到字典中
		d[key] = value

	return d
