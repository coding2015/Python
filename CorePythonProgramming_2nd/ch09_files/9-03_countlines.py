#!/usr/bin/python

'counting the total lines of a given file'

name = raw_input('enter a filename> ')
f  = open(name,'r')

print 'total lines:', len(f.readlines())

f.close()

