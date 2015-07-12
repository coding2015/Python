#!/usr/bin/python
#coding:utf-8

'''
提取whodata.txt 各项信息
'megan    :0           2015-07-07 12:30 (:0)\n'
'megan    pts/0        2015-07-07 12:30 (:0)\n'
分析:以上数据为经repr()的原始数据，空白符只有空格及'\n', 数据以数个空格分开
'''


import re

filename = 'whodata.txt'
print filename
for line in open(filename):
	print repr(line)

# 分组法
print '\ngroups():'
patt = re.compile('(\w+)\s+(\w*[/:]\d)\s+([\d\-\s:]+)\s+(\([:\d]+\))')
								# 最后一个\s+把前面的\s给夺过来了
for line in open(filename):
	m = patt.match(line)
	if m is not None: print m.groups()
	else: print None


# 分割法
import os
print '\nsplit()'
for line in os.popen('who', 'r'):
	#print re.split(' +|\n', line) 
	print re.split('\s+', line)


'''
$ python rewho.py 
whodata.txt
'megan    :0           2015-07-07 12:30 (:0)\n'
'megan    pts/0        2015-07-07 12:30 (:0)\n'
'megan    pts/1        2015-07-07 14:14 (:0)\n'
'megan    pts/2        2015-07-07 14:14 (:0)\n'
'megan    pts/3        2015-07-07 14:14 (:0)\n'
'megan    pts/4        2015-07-07 14:14 (:0)\n'
'megan    pts/5        2015-07-11 23:50 (:0)\n'
'megan    pts/6        2015-07-12 07:08 (:0)\n'
'megan    pts/7        2015-07-10 07:11 (:0)\n'

groups():
('megan', ':0', '2015-07-07 12:30', '(:0)')
('megan', 'pts/0', '2015-07-07 12:30', '(:0)')
('megan', 'pts/1', '2015-07-07 14:14', '(:0)')
('megan', 'pts/2', '2015-07-07 14:14', '(:0)')
('megan', 'pts/3', '2015-07-07 14:14', '(:0)')
('megan', 'pts/4', '2015-07-07 14:14', '(:0)')
('megan', 'pts/5', '2015-07-11 23:50', '(:0)')
('megan', 'pts/6', '2015-07-12 07:08', '(:0)')
('megan', 'pts/7', '2015-07-10 07:11', '(:0)')

split()
['megan', ':0', '2015-07-07', '12:30', '(:0)', '']
['megan', 'pts/0', '2015-07-07', '12:30', '(:0)', '']
['megan', 'pts/1', '2015-07-07', '14:14', '(:0)', '']
['megan', 'pts/2', '2015-07-07', '14:14', '(:0)', '']
['megan', 'pts/3', '2015-07-07', '14:14', '(:0)', '']
['megan', 'pts/4', '2015-07-07', '14:14', '(:0)', '']
['megan', 'pts/5', '2015-07-11', '23:50', '(:0)', '']
['megan', 'pts/6', '2015-07-12', '07:08', '(:0)', '']
['megan', 'pts/7', '2015-07-10', '07:11', '(:0)', '']
''' 


