#!/usr/bin/python

'a test to see exception processed by caller level'


def OpenFile(fname):
	open(fname)

def Test():
	OpenFile('xxx')


try:
	Test()
except IOError,r:
	print 'r:',r

