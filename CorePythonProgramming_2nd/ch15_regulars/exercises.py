#!/usr/bin/python

'''
Exercises from chapter-15
'''

15-1 识别下列字符串:“bat,” “bit,” “but,” “hat,” “hit,” 或 “hut”
		解析：
			所有长度相等
			首字母有2种，次字母有3种，尾字母有1种，共2*3*1=6种排列组合
			要匹配字符串个数等于排列组合数， 故匹配模式可采取[..][..]组合方式，即：
		patt = '[bh][aiu]t'


15-2 匹配用一个空格分隔的任意一对单词,比如,名和姓。
		re.spilt('\s', data)	# looser-match, 不排除带非字母的名字
		patt = '[A-Za-z-]+ [A-Za-z-]+' # restrictive-match, 只允许名字中带字母或-


15-3 匹配用一个逗号和一个空格分开的一个单词和一个字母。例如,英文人名中的姓和名
		patt = '[A-Za-z]+[ ,][A-Za-z]+'
		正解:
		1.Any word and single letter separated by a comma and single space,
													 e.g., last name,first initial
			patt = '[A-Za-z-]+, [A-Za-z]' # 单词中可以包含连字符
		2.Any pair of words separated by a comma and single space,
											 e.g., last, first names,hyphens allowed
			patt = '[A-Za-z-]+, [A-Za-z-]+'


15-4 匹配所有合法的Python标识符
		合法标识符: 只包含下划线和字母数字，且由下划线或字母开头
		# patt = '^[_\w]\w+'	# error 1.\w 包含了数字；2.可能只有一个字符
		patt = '^[_A-Za-z]\w*'


15-6 匹配简单的以“www.”开头,以“.com”作结尾的 Web 域名,例如:www.yahoo.com. 附
加题:使你写的正则表达式还支持其他顶级域名:.edu, .net 等,比如:www.ucsc.edu.
		patt = 'www\..+?\.(com|net|edu|gov|org)$'
		'''	
		>>> re.match(patt, 'www.xxx.com').group()
		'www.xxx.com'	
		>>> re.match(patt, 'www.xxx.user@www.yyy.zzz.gov').group()
		'www.xxx.user@www.yyy.zzz.gov'
		'''
		keypoint: 将|用在分组中


15-7 匹配全体 Python 整数的字符串表示形式的集合
		patt = '^\d+$'


15-8 匹配全体 Python 长整数的字符串表示形式的集合
		patt = '^\d+[lL]$'

15-9 匹配全体 Python 长整数的字符串表示形式的集合
		patt = '\d+\.\d*'


15-10 匹配全体 Python 复数的字符串表示形式的集合
		patt = '[\d.]*\+?[\d.]+j'
		'''
		>>> re.match('[\d.]*\+?[\d.]+j', '12j').group()
		'12j'
		>>> re.match('[\d.]*\+?[\d.]+j', '1.0+23.45j').group()
		'1.0+23.45j'
		'''

15-13 提取type结果中的类型值
		data: >>> repr(type(1)) "<type 'int'>"
		patt = r'<type\s+[\'\"](.+)[\'\"]>'	# [\'\"], 宽松匹配 
		>>> def whatType(obj):
		...     typestr = str(type(obj))
		...     patt = r'<type\s+[\'\"](.+)[\'\"]>'
		...     m = re.match(patt, typestr)
		...     if m is not None: 
		...             return m.group(1)
		... 
		>>> whatType(1)
		'int'
		>>> whatType(2.3)
		'float'
		>>> whatType([])
		'list'
		>>> whatType(dir)
		'builtin_function_or_method'

15-14 匹配月份1-12
		可能存在月份(数字)形式： 7，07, 2015-07, 2015/07
		patt = r'\b(0?[1-9]|1[0-2])\b'  # 0?[1-9]匹配1-9， 1[0-2]匹配10-12
		'''
		>>> re.search(r'\b(0?[1-9]|1[0-2])\b', '07').group()
		'07'
		>>> re.search(r'\b(0?[1-9]|1[0-2])\b', '7').group()
		'7'
		>>> re.search(r'\b(0?[1-9]|1[0-2])\b', '12').group()
		'12'
		>>> re.search(r'\b(0?[1-9]|1[0-2])\b', '13').group()
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		AttributeError: 'NoneType' object has no attribute 'group'
		>>> re.search(r'\b(0?[1-9]|1[0-2])\b', '2015-07-13').group()
		'07'
		>>> re.search(r'\b(0?[1-9]|1[0-2])\b', '2015/07/13').group()
		'07'
		'''
				 
