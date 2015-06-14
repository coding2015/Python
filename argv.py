#!/usr/bin/python

'test for sys.argv'

import sys

print 'you entered ', len(sys.argv),' arguments'
print 'they are:'
for e in enumerate(sys.argv):
	print e


x = None
d ={'e':None}
print 'None:',None
print 'x:',x
print d['e']
