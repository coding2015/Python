'Exercise 6-5 from Core Python Programming 2nd'

def StrCom(s1,s2,caseSensitivity=False):
	'''
compare two strings to see if they are the same
return bool value
method: compare each character of the two strings
caseSensitivity;default false
	'''
	if len(s1) != len(s2):
		return False
	elif caseSensitivity == False:
		for i in range(len(s1)):
			if s1[i].lower() != s2[i].lower():
				return False
		else:
			return True
	else:
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				return False
		else:
			return True


def test_strcom():
	print StrCom.__doc__
	s1 = raw_input('enter a string:\n> ')
	s2 = raw_input('enter a string:\n> ')
	cased = raw_input('whether compare in case-sensitivity,yes? (no default)> ')
	if cased == 'y':
		print 'matched(case-sensitivity)?',StrCom(s1,s2,True)
	else:
		print 'matched(case-insensitivity)?', StrCom(s1,s2)

if __name__ == '__main__':
	test_strcom()

	
