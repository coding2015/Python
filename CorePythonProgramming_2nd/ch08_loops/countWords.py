#!/usr/bin/python

'''
script for counting words of a given file

key point: list comprehensions
'''

fname = raw_input('enter a file path> ')

count = sum(len(words) for line in open(fname,'r') for words in line.split())

print 'words:',count
