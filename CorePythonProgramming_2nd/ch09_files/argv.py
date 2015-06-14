#!/usr/bin/python

'test for sys.argv'

import sys

print 'you entered ', len(sys.argv),' arguments'
print 'they are:'
for e in enumerate(sys.argv):
	print e



