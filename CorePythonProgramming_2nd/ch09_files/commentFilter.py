#!/usr/bin/python

'''
Exercise 9-1:
	display all the lines of file, filtering the line beginning with "#" 

Problem:
	extra credit: strip out comments begin after the first character 
'''

name = raw_input('enter a filename> ')
f = open(name,'r')

i = 1 # counting file lines
for eachLine in f:
	if eachLine.[0] != '#':
		print i, eachLine.strip()
	else:
		print i, '#comments'
	i += 1

f.close()
