'Exercise 6-6 in core python programming 2nd'
'implement strip'

import string
whiteSpaces = string.whitespace

def Strip(s):
	''' 
    implement str's method:strip()
    idea: find the beg and end index which are not whitespace
	'''
	for beg in range(len(s)):
		if s[beg] not in whiteSpaces:
			break
	for end,e in enumerate(s[::-1]):
		if e not in whiteSpaces:
			break
	return s[beg:len(s)-end] #!!!


def test_strip():
	print Strip.__doc__
	s = raw_input('enter a string:\n> ')
	print 'raw:(%r)[%d]' % (s,len(s))
	print 'S:(%r)[%d]'% (Strip(s),len(Strip(s)))
	print 's:(%r)[%d]'%  (s.strip(),len(s.strip()))

if __name__ == '__main__':
    test_strip()


