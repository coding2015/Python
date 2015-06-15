#!/usr/bin/python

'''
compare two files, if they are different:
show the different line and column numbers where the first difference occurs
'''

def ColumnNumber(s1,s2):
	for i , c1 in enumerate(s1):
		if c1 != s2[i]:
			break
	# possible case: s1 in s2
	pass


name1 = raw_input('enter a filename> ')
name2 = raw_input('enter a filename> ')
f1 = open(name1, 'r')
f2 = open(name2, 'r')

#compare lines
pass
#compare characters
pass

f1.close()
f2.close()


