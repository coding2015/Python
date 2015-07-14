#coding:utf-8

'''
Exercise 6-6 
	implement strip
'''

import string
whitespace = string.whitespace

def strip(s):
	''' 
    implement str's method:strip()
    idea: find the beg and end index which are not whitespace
	'''
	for beg in range(len(s)):
		if s[beg] not in whitespace:
			break
	for end in range(len(s)-1, -1, -1):
		if s[end] not in whitespace:
			break
	print '(beg, end)', (beg, end)
	if beg == end:	# 当s=' '(一个空格时)， beg == end == 0
		return ''
	return s[beg:end+1] # ！注意，[beg:end] 不包括end


def test_strip():
	print strip.__doc__
	s = raw_input('enter a string:\n> ')
	stripped = strip(s)
	print 's:        ', `s`
	print 'mystrip:  ', `stripped`
	print 'str.strip:', `s.strip()`

if __name__ == '__main__':
    test_strip()


'''
enter a string:
>  
(beg, end) (0, 0)
s:         ' '
mystrip:   ''
str.strip: ''


enter a string:
> 		  
(beg, end) (3, 0)
s:         '\t\t  '
mystrip:   ''
str.strip: ''


enter a string:
> hello
(beg, end) (0, 4)
s:         'hello'
mystrip:   'hello'
str.strip: 'hello'


enter a string:
> 	 hello
(beg, end) (2, 6)
s:         '\t hello'
mystrip:   'hello'
str.strip: 'hello'


enter a string:
> hello		  
(beg, end) (0, 4)
s:         'hello\t\t  '
mystrip:   'hello'
str.strip: 'hello'

'''
