#!/usr/bin/python

# 匹配多个字符串(|)
>>> bt = 'bat|bet|bit'
>>> m = re.match(bt, 'bat')		# match()匹配到'bat'
>>> if m is not None:
...     m.group()
... 
'bat'
>>> m = re.match(bt, 'blt')		# match()不匹配字符串
>>> if m is not None:
...     m.group()
... 
>>> m = re.match(bt, 'I bit him')	# mathc()不匹配字符串
>>> if m is not None:
...     m.group()
... 
>>> m = re.search(bt, 'I bit him')	# search()搜索到'bit'
>>> if m is not None:
...     m.group()
... 
'bit'
>>> 


# 匹配除'\n'外的任意单个字符(.)
>>> anyend = '.end'
>>> m = re.match(anyend, 'bend')	# .匹配'b'
>>> if m is not None:
...     m.group()
... 
'bend'
>>> m = re.match(anyend, 'end')		# .没有字符匹配
>>> if m is not None:
...     m.group()
... 
>>> m = re.match(anyend, '\nend')	# .不匹配\n
>>> if m is not None:
...     m.group()
... 
>>> m = re.search(anyend, 'The end.') # .匹配' '
>>> if m is not None:
...     m.group()
... 
' end'
>>> m = re.match('(.end)(.end)(.end)(.end)', '\rend\tend\x0bend\x0cend')
>>> if m is not None:					# .匹配空白字符	 
...     m.groups()										 
... 
('\rend', '\tend', '\x0bend', '\x0cend')
>>> m = re.match('(.end)*', '\rend\tend\x0bend\x0cend')	# 一个分组
>>> m.groups()				# 子组为最后一个匹配对象
('\x0cend',)				# 原因: 子组数据被不断地替换成下一个匹配了的对象
>>> m.group()
'\rend\tend\x0bend\x0cend'
>>>
>>> re.match('3.14', '3.14').group()	# .可以匹配.
'3.14'
>>> re.match('3.14', '3014').group()	# .也可以匹配0
'3014'
>>> re.match('3\.14', '3014').group()	# \.只匹配.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> re.match('3\.14', '3.14').group()
'3.14'
>>> 


# 重复、特殊字符和子组

	# 匹配 user@xxx.com 与 user@主机名.xxx.com
>>> patt = '\w+@(\w+\.)?\w+\.com'
>>> re.match(patt, 'nobody@xxx.com').group()
'nobody@xxx.com'
>>> re.match(patt, 'nobody@www.xxx.com').group()
'nobody@www.xxx.com'

	# 匹配 user@[主机名.][任意个子域名.]xxx.com
>>> patt = '\w+@(\w+\.)*\w+\.com'
>>> re.match(patt, 'nobody@xxx.com').group()
'nobody@xxx.com'
>>> re.match(patt, 'nobody@www.xxx.com').group()
'nobody@www.xxx.com'
>>> re.match(patt, 'nobody@www.xxx.yyy.zzz.com').group()
'nobody@www.xxx.yyy.zzz.com'
	
	# 分组
>>> m = re.match('(\w{3})-(\d{3})', 'abc-123')
>>> m.group()	# 所有匹配部分
'abc-123'
>>> m.group(1)	# 匹配子组1
'abc'
>>> m.group(2)	# 匹配子组2
'123'
>>> m.groups()	# 所有匹配子组
('abc', '123')
>>> m = re.match('ab', 'ab')	# 无子组
>>> m.group()
'ab'
>>> m.groups()
()
>>> m = re.match('(ab)', 'ab')	# 一个子组
>>> m.groups()
('ab',)
>>> m = re.match('(a)(b)', 'ab') # 两个子组(分开)
>>> m.groups()
('a', 'b')
>>> m = re.match('(a(b))', 'ab') # 两个子组(复合)
>>> m.groups()
('ab', 'b')
>>> 




