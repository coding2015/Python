#!/usr/bin/python
#coding:utf-8

'''
Example 15.2
	Data Generator for RE Exercises
	Create random data for regular expressions practice and output the generated data
to the screen.
'''

from random import randint, choice
from string import lowercase	# Data: 'abcdefghijklmnopqrstuvwxyz'
from sys import maxint		# Data:9223372036854775807
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

for i  in range(randint(5, 10)):
	dtint = randint(0, maxint % 10000000000)	# 秒数
	print dtint
	dtstr = ctime(dtint)	# 将秒数转换为从1970-6-1计起的时间
							# 参数sec存在上限，超出上限会报错
	
	shorter = randint(4, 7)
	em = ''
	for j in range(shorter):
		em += choice(lowercase)

	longer = randint(shorter, 12) 
	dn = ''
	for j in range(longer):
		dn += choice(lowercase)

	print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms),
								 dtint, shorter, longer)


'''
$ python gendata.py 
2610878899
Wed Sep 25 20:08:19 2052::mfdv@caqh.gov::2610878899-4-4
6049960334
Sat Sep 19 00:32:14 2161::rdof@chcau.gov::6049960334-4-5
3310355143
Sun Nov 25 15:05:43 2074::rjtkx@cygtx.gov::3310355143-5-5
3515581633
Tue May 27 22:27:13 2081::edag@tvkycrtrsdk.net::3515581633-4-11
5040812353
Tue Sep 27 01:39:13 2129::eoigt@skyvfjxuta.org::5040812353-5-10
1440060655
Thu Aug 20 16:50:55 2015::oykkj@bmbzxsy.com::1440060655-5-7
916810796
Wed Jan 20 13:39:56 1999::nlowvj@trxizro.net::916810796-6-7
2599883370
Tue May 21 13:49:30 2052::sjszaim@buybuno.org::2599883370-7-7
2545522509
Wed Aug 31 09:35:09 2050::zayvj@kyfeq.net::2545522509-5-5
'''
