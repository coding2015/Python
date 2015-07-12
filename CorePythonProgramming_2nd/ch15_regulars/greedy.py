#!usr/bin/python

'''
greedy match
'''

>>> data = 'Tue Sep 27 01:39:13 2129::eoigt@skyvfjxuta.org::5040812353-5-10'
>>> re.search('\d+-\d+-\d+', data).group()
'5040812353-5-10'		# 正常匹配
>>> re.search('.*(\d+-\d+-\d+)', data).group()
'Tue Sep 27 01:39:13 2129::eoigt@skyvfjxuta.org::5040812353-5-10'
>>> re.search('.*(\d+-\d+-\d+)', data).groups()
('3-5-10',)				# 贪心匹配，导致分组的匹配数据不完整
>>> re.search('.*?(\d+-\d+-\d+)', data).groups()
('5040812353-5-10',)	# 非贪心匹配

