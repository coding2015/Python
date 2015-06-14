#!/usr/bin/python
#coding:utf-8

'找出列表中所有的obj及其索引号'

#create a list
l = raw_input('enter a list,separated by space:\n> ').split()

#give a obj
obj = raw_input('enter the obj:\n> ')

#find
'''
1.make sure the obj is in the list: in
2.count how nany objs in the list:count
3.find the indexes of the objs
'''
if obj in l:
	num = l.count(obj)	
	i = 1
	index = 0
	print 'index:'
	while i <= num:
		index = l.index(obj,index)
		print index,
		index += 1 #需要在找到的索引上向后一位，否则找的当将是第一个索引
		i += 1
else:
	print 'there is no %s in the list.' % obj



