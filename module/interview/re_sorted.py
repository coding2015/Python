#!/usr/bin/python
#coding:utf-8

'''
问题：
	对一组包含数字的字符串按其数字排序

思路：
	先re提取数字为键，内容为值
	对键排序
	逐个将排好序的键对应的值添加到列表中

备注:
	只适用于数字唯一的数据
	不适用于存在多个数字一样的数据
'''

import re

data = ['test_05_ex', 'test_02_ex', 'test_12_ex', 'test_45_ex','test_010_ex']
print 'original:', data
print


# 创建字典：提取数字为键，数据为键值
patt = r'.*_(\d+)_.*'
dic = {}
for e in data:
	key = int(re.match(patt, e).group(1))
	dic[key] = e
print 'dic:', dic


# 按键(数字)排序
# keys = dic.keys().sort()   # error: 不能直接对返回的list排序，得到的是None
keys = dic.keys()
keys.sort()
data_sorted = []
for k in keys:
	data_sorted.append(dic[k])	

print '\nsorted:  ', data_sorted


