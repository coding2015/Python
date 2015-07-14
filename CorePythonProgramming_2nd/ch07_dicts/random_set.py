#!/usr/bin/python
#coding:utf-8

'''
Exercise 7-13
'''

from random import randint

def generateSet():
	return set(randint(0,9) for i in range(randint(1,10))) 


A = generateSet()
B = generateSet()

print 'A:'.ljust(6), A
print 'B:'.ljust(6), B
print 'A|B:'.ljust(6), A | B
print 'A&B:'.ljust(6), A & B


'''
$ python random_set.py 
A:     set([1, 6])
B:     set([1, 2, 9, 4, 7])
A|B:   set([1, 2, 4, 6, 7, 9])
A&B:   set([1])
'''
