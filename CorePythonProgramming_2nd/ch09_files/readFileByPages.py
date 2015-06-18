#!/usr/bin/python

'''
Exercise 9-4:
	like command "more": read file one page at a time
'''

name = raw_input('enter a filename> ')
f = open(name,'r')

i = 1
for line in f:
	print i,line,
	if i % 25 == 0:
		raw_input('press any key to continue.')
	i += 1

f.close()
